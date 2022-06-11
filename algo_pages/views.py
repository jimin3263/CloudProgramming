from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from algo_pages.models import Post, Tag


def index(request):
    return render(
        request,
        'algo_pages/algorithm_page.html'
    )

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched) | Q(number__icontains=searched)).distinct()
    else:
        posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'algo_pages/search.html', {'posts': posts})

def showPostByTag(request, tag):
    tag = Tag.objects.get(name=tag)
    post_list = tag.post_set.filter(author=request.user)
    tags = Tag.objects.all()
    context = {
        'tags': tags,
        'post_list': post_list
    }
    return render(request, 'algo_pages/algorithm_page.html', context)

def myPostList(request):
    post_list = Post.objects.filter(author=request.user)
    tags = Tag.objects.all()
    return render(
        request,
        'algo_pages/algorithm_page.html',
        {
            'post_list': post_list,
            'tags': tags
        }
    )

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'algo_pages/algorithm_page.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'algo_pages/algorithm_detail.html'
