import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from markdown import markdown
from markdownx.models import MarkdownxField

class Tier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/myalgo/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    number = models.IntegerField() #문제번호
    content = MarkdownxField() #내용

    tag = models.ManyToManyField(Tag, blank=True)

    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/algorithm/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)