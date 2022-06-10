from django.shortcuts import render
from django.views.generic import ListView, DetailView
from algo_pages.models import Post

def index(request):
    return render(
        request,
        'algo_pages/algorithm_page.html'
    )

def search(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'algo_pages/search.html',
        {
            'posts': recent_posts
        }
    )

def myPostList(request):
    post_list = Post.objects.filter(author=request.user)
    return render(
        request,
        'algo_pages/algorithm_page.html',
        {
            'post_list': post_list
        }
    )

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'algo_pages/algorithm_page.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'algo_pages/algorithm_detail.html'
