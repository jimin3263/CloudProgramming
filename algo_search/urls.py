from django.urls import path

from algo_search import views

urlpatterns = [
    path('', views.search),
    path('tag/<str:tag>/', views.showPostByTag),
]