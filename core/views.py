from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Post, Tag, Comment, CATEGORY_OPTIONS
# from .forms import PostForm, TagForm, CommentForm

# Create your views here.
def blogCategoriesView(request):
    categories = [option[1] for option in CATEGORY_OPTIONS]
    post_categories = []
    for category in categories: 
        post_categories.append(
            list(Post.objects.filter(category=category))
        )
    print(post_categories)
    cat_and_posts = zip(categories, post_categories)
    context = {
        'category_options': categories, 
        'cats_and_posts': cat_and_posts,
        # 'post_categories': post_categories
    }
    return render(request, 'core/blog_categories.html', context)

def commentCreateView(request, id): # id of post being viewed
    if request.method == 'POST': 
        post = Post.objects.get(id=id)
        if request.POST['username'] or request.POST['content']:
            new_comment = Comment.objects.create(
                username=request.POST['username'], 
                content=request.POST['content'], 
                post=post
            )
            new_comment.save()
        else: 
            messages.success(request, ("Empty comments or usernames are not accepted"))
        return redirect(reverse('core:detail', kwargs={'id': id}))
    else:
        return redirect(reverse('core:detail', kwargs={'id': id}))

@login_required(login_url='authentic:login')
def blogDeleteView(request, id):
    post = Post.objects.get(id=id) 
    if request.method == 'POST':  
        post.delete()
        print('Post has been deleted')
        return redirect(reverse('core:home')) 
    print('Post not deleted')
    return render(request, 'core/blog_delete.html', {'post': post}) 

@login_required(login_url='authentic:login')
def blogUpdateView(request, id):
    post = Post.objects.get(id=id) 
    if request.method == 'POST' and post.author == request.user.username: 
        response = request.POST
        # print(response)
        title = response['title'] 
        content = response['content'] 
        tags_checked = [name[4:] for name in list(response.keys()) if name.startswith('tag_')]
        tags_typed = response['new_tags'].split(',')
        tags_typed = [tag_name.strip() for tag_name in tags_typed]
        all_tags = tags_checked + tags_typed
        # print('All tags', all_tags)
        post.title = title 
        post.content = content
        for tag_name in all_tags:
            if tag_name.strip():
                tag, created = Tag.objects.get_or_create(name=tag_name.lower()) 
                post.tags.add(tag) 
        post.save()
        return redirect(reverse('core:detail', kwargs={'id': id}))

    context = {
        'post': post, 
        'category_options': [option[1] for option in CATEGORY_OPTIONS], 
        'all_tags': Tag.objects.all(), 
        'cat_name': post.category.title()
    }
    return render(request, 'core/blog_update.html', context) 

@login_required(login_url='authentic:login')
def blogCreateView(request):
    if request.method == 'POST': 
        response = request.POST
        title = response['title'] 
        content = response['content']
        category = response['category'] 
        new_post = Post.objects.create(
            title=title, 
            content=content, 
            category=category, 
            author=request.user.username
        )
        new_post.save()
        tag_names = [name[4:] for name in list(response.keys()) if name.startswith('tag_')]
        new_tags_lists = response['new_tags'].split(',')
        new_tags = [tag_name.strip() for tag_name in new_tags_lists]
        new_tags.extend(tag_names)
        # Create new tags 
        for tag_name in new_tags:
            # print('tag_name', tag_name)
            if tag_name.strip():
                tag, created = Tag.objects.get_or_create(name=tag_name.lower()) 
                new_post.tags.add(tag) 
        new_post.save()
        return redirect(reverse('core:detail', kwargs={'id':new_post.id}))

    context = {
        'category_options': [option[1] for option in CATEGORY_OPTIONS], 
        'all_tags': Tag.objects.all()
    }
    return render(request, 'core/blog_create.html', context)

def blogDetailsView(request, id):
    post = get_object_or_404(Post, id=id)
    edit_authorisation = False
    if post.author == request.user.username: 
        edit_authorisation = True
    return render(request, 'core/blog_detail.html', {
                'post': post, 
                'edit_authorisation': edit_authorisation
            })

def blogListView(request):
    blog_feed = Post.objects.all()
    context = {
        'blog_feed': blog_feed
    }
    return render(request, 'core/blog_list.html', context)

