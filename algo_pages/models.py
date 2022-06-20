from django.contrib.auth.models import User
from django.db import models
from markdown import markdown
from markdownx.models import MarkdownxField

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/search/tag/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    number = models.IntegerField(null=True, blank=True) #문제번호
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

    def get_pk(self):
        return self.pk

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'