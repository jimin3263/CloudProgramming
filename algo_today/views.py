import random

from django.shortcuts import render

# Create your views here.
from algo_pages.models import Post
from algo_today.clawler import crawl
from algo_today.models import Problem, TodayProblem


def index(request):
    #today_problem = TodayProblem.objects.last().problem
    today_problem = Problem.objects.get(pk=random.randrange(1, 4900))
    tags = today_problem.tag.split(" ")
    count = Post.objects.filter(number=today_problem.number).count()
    context = {
        'today_problem': today_problem,
        'tags': tags,
        'count': count
    }

    return render(
        request,
        'algo_today/algorithm_today.html',
        context
    )