from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """A user model with no custom fields"""
    pass

    def __str__(self):
        return self.username


class Post(models.Model):
    """A post model for creating posts"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """A comment model bound to the post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    """A model for counting post views"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    """A model for counting post likes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
