from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import PostForm, CommentForm
from .models import Post, PostView, Like


class PostListView(ListView):
    """A class to display a list of posts"""
    model = Post


class PostDetailView(DetailView):
    """A class to display a single post"""
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object


class PostCreateView(CreateView):
    """A class to create a single post"""
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Create'
        })
        return context


class PostUpdateView(UpdateView):
    """A class to update a single post"""
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Update'
        })
        return context


class PostDeleteView(DeleteView):
    """A class to delete a single post"""
    model = Post
    success_url = '/'


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
