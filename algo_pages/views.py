from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from algo_pages.models import Post, Tag

def index(request):
    return render(
        request,
        'algo_pages/algorithm_page.html'
    )


def myPostList(request):

    tags = Tag.objects.all()
    if request.user.is_authenticated:
        post_list = Post.objects.filter(author=request.user)
        return render(
            request,
            'algo_pages/algorithm_page.html',
            {
                'post_list': post_list,
                'tags': tags
            }
        )
    else:
        return render(
            request,
            'algo_pages/algorithm_page.html',
            {
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

def signin(request):
    if request.method == "GET":
        return render(request,'algo_pages/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return redirect('/')
        else:
            return render(request,'algo_pages/login.html', {'error': '아이디, 비밀번호를 제대로 입력해주세요.'})

def signup(request):
    if request.method == "GET":
        return render(request,'algo_pages/signup.html')

    elif request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try: user = User.objects.create_user(
                username= request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
            except:
                return render(request, 'algo_pages/signup.html', {'error': '중복되는 아이디 혹은 이메일입니다.'})
            auth.login(request, user)
            return redirect('/')
        return render(request, 'algo_pages/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})

def logout(request):
    if request.method == "GET":
        return render(request,'algo_pages/logout.html')

    elif request.method == "POST":
        auth.logout(request)
        return redirect('/')
