from django.shortcuts import render
from django.urls import path
from . import views


def login(request):
    return render(request, 'login.html')


urlpatterns = [
    path('', views.login),
    path('welcome', views.welcome),
    path('tourist_info', views.tourist_info),
    path('event_archiving', views.event_archiving),
    path('project_management', views.project_management),
    path('notice_management', views.notice_management),
]
