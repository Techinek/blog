from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post


class PostListView(ListView):
    """A class to display a list of posts"""
    model = Post


class PostDetailView(DetailView):
    """A class to display a single post"""
    model = Post


class PostCreateView(CreateView):
    """A class to create a single post"""
    model = Post
    fields = [
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    ]


class PostUpdateView(UpdateView):
    """A class to update a single post"""
    model = Post
    fields = [
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    ]

class PostDeleteView(DeleteView):
    """A class to delete a single post"""
    model = Post
    success_url = '/'
