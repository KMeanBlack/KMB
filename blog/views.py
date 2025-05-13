from django.shortcuts import render, HttpResponse, redirect
from blog.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.http import JsonResponse
from .forms import TextForm, AddBlogForm
from django.utils.text import slugify

def blogHome(request): 
    allPosts= Post.objects.all()
    category = Category.objects.all().filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(allPosts, 4)
    blogs = Post.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    post_by_category = Post.objects.filter().order_by('-category')
    
    
    try:
        allPosts = paginator.page(page)
    except EmptyPage:
        allPosts = paginator.page(1)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
        return redirect('blog/blogHome.html')
    context={'allPosts': allPosts, "paginator": paginator, "blogs": blogs,"tags": tags, "category": category,  'post_by_category':post_by_category,
     }
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
    form = TextForm()
    blog = get_object_or_404(Post, slug=slug)
    category = Category.objects.get(id=blog.category.id)
    related_blogs = category.category_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    liked_by = request.user in blog.likes.all()
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    
    if request.method == "POST" and request.user.is_authenticated:
        form = TextForm(request.POST)
        if form.is_valid():
            BlogComment.objects.create(
                user=request.user,
                blog=blog,
                text=form.cleaned_data.get('text')
            )

            return redirect('blogPost', slug=slug)

    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict, "blog": blog,
        "related_blogs": related_blogs,
        "tags": tags,
        "form": form,
        "liked_by": liked_by}
    return render(request, "blog/blogPost.html", context)

def category_blogs(request, slug):
    allPosts= Post.objects.all()
    category = get_object_or_404(Category, slug=slug)
    queryset = category.category_blogs.all()
    tags = Tag.objects.order_by()[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    all_blogs = Post.objects.order_by()[:5]
    post=Post.objects.filter(slug=slug).first()
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('bloghome')

    context = {
        "blogs": blogs,
        "tags": tags,
        "all_blogs": all_blogs,
        "allPosts": allPosts,
        'post':post,
    }
    return render(request, 'blog/category_blogs.html', context)


def tag_blogs(request, slug):
    allPosts= Post.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    queryset = tag.tag_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    all_blogs = Post.objects.order_by('-created_date')[:5]
    post=Post.objects.filter(slug=slug).first()

    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('bloghome')

    context = {
        "blogs": blogs,
        "tags": tags,
        "all_blogs": all_blogs,
        "allPosts": allPosts,
        'post':post,
        
    }
    return render(request, 'blog/category_blogs.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

