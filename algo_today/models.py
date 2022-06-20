from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=500)
    tag = models.CharField(max_length=500)
    number = models.IntegerField()

    def __str__(self):
        return f'[{self.number}] {self.title}'

    def get_absolute_url(self):
        return f'/today/'

class TodayProblem(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.problem.pk}'

