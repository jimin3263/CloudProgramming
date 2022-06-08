import random

from django.shortcuts import render

# Create your views here.
from algo_today.models import Problem, TodayProblem
from algo_today import sheduler


def index(request):

    #TodayProblem.objects.last().number
    today_problem = Problem.objects.get(pk=1)
    tags = today_problem.tag.split(" ")
    context = {
        'today_problem': today_problem,
        'tags': tags
    }

    return render(
        request,
        'algo_today/algorithm_today.html',
        context
    )