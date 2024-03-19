from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# Post => title, content, author, date_published 
# Category => name 
# Tag => name 
# Comment => username, content

CATEGORY_OPTIONS = [
        ('tech', 'Technology'), 
        ('business', 'Business'), 
        ('health and wellness', 'Health And Wellness'), 
        ('travel', 'Travel'), 
        ('food and clothing', 'Food And Clothing'), 
        ('lifestyle', 'Lifestyle'), 
        ('finance and investing', 'Finance And Investing'), 
        ('education', 'Education'), 
        ('faith', 'Faith'), 
        ('entertainment', 'Entertainment'),
        ('environment and sustainability', 'Environment And Sustainability'), 
        ('arts and culture', 'Arts And Culture')
    ]

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100, null=False, default='') 
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=100, default='')
    date_published = models.DateField(auto_now=True) 
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    username = models.CharField(max_length=100) 
    content = models.TextField(null=False, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 