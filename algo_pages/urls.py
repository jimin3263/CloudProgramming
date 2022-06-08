from django.urls import path

from algo_pages import views

urlpatterns = [
    path('myalgo/', views.PostList.as_view()),
    path('search/', views.search)
]