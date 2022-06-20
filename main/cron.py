import random

from algo_today.models import Problem,TodayProblem

def create_today_problem():
    TodayProblem.objects.create(problem= Problem.objects.get(pk=random.randrange(1, 6125)))