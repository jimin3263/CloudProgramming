from django.urls import path

from algo_today import views

urlpatterns = [
    path('', views.index)
]