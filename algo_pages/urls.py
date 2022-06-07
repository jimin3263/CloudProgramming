from django.urls import path

from algo_pages import views

urlpatterns = [
    path('myalgo/', views.index),
    path('search/', views.search)
]