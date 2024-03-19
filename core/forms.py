from django import forms
from .models import (
    Post, Tag, Comment
)

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post 
        fields = [
            'title', 'content', 'category', #'tags'
        ]

class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag 
        fields = ['name']

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = [
            'username', 'content'
        ]