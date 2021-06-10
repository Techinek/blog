from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import PostForm

from .models import Post


class PostListView(ListView):
    """A class to display a list of posts"""
    model = Post


class PostDetailView(DetailView):
    """A class to display a single post"""
    model = Post


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
