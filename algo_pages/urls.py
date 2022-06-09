from django.urls import path

from algo_pages import views

urlpatterns = [
    path('algorithm/', views.PostList.as_view()),
    path('algorithm/<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('search/', views.search)
]