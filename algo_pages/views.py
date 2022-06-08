from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from algo_pages.models import Post


def index(request):
    return render(
        request,
        'algo_pages/algorithm_page.html'
    )

def search(request):
    return render(
        request,
        'algo_pages/search.html'
    )


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'algo_pages/algorithm_page.html'
