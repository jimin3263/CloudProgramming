from django.urls import path

from algo_pages import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('algorithm/', views.myPostList),
    path('algorithm/<int:pk>/', views.PostDetail.as_view()),
    path('', views.myPostList),
    path('algorithm/create/', views.PostCreate.as_view()),
    path('algorithm/update/<int:pk>/', views.PostUpdate.as_view()),
    path('algorithm/delete/<int:pk>/', views.delete),
    path('login/', views.signin),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('tag/', views.tag),
    path('algorithm/<int:pk>/new_comment/', views.new_comment)
]