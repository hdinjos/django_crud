from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def blog_list(req):
    post = Post.objects.all()
    context = {'blog_list' : post}
    return render(req, 'blog/blog_list.html', context)

def blog_detail(req, id):
    each_post = Post.objects.get(id=id)
    context= {}
    context['blog_detail'] = each_post
    return render(req, 'blog/blog_detail.html', context)

def blog_delete(req, id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return redirect('/post')
