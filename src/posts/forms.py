from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """A form based on Post model"""

    class Meta:
        model = Post
        fields = ('__all__')


class CommentForm(forms.ModelForm):
    """A form based on Comment model"""
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content',)
