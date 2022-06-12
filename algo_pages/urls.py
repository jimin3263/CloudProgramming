from django.urls import path

from algo_pages import views

urlpatterns = [
    path('algorithm/', views.myPostList),
    path('algorithm/<int:pk>/', views.PostDetail.as_view()),
    path('', views.myPostList),
    path('search/', views.search),
    path('search/tag/<str:tag>/', views.showPostByTag),
    path('algorithm/create/', views.PostCreate.as_view())
]