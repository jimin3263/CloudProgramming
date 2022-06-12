from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
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

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'number', 'content', 'tag', 'image']
    template_name = 'algo_pages/algorithm_create.html'
    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_authenticated:
            form.instance.author= current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/algorithm/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'number', 'content', 'tag', 'image']

    template_name = 'algo_pages/algorithm_update.html'

    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied