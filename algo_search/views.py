from django.db.models import Q
from django.shortcuts import render

from algo_pages.models import Post, Tag


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched) | Q(number__icontains=searched)).distinct()
    else:
        posts = Post.objects.order_by('-pk')[:3]
    return render(request,
                  'algo_today/search.html',
                  {'posts': posts})

def showPostByTag(request, tag):
    tag = Tag.objects.get(name=tag)
    post_list = tag.post_set.filter(author=request.user)
    tags = Tag.objects.all()
    context = {
        'tags': tags,
        'post_list': post_list
    }
    return render(request, 'algo_pages/algorithm_page.html', context)
