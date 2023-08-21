from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context={
        'post':post
    }
    return render(request, 'blog/blog_detail.html', context)

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts' : posts
        }
    return render(request, 'blog/list.html', context)