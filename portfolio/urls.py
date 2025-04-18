from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('analytics/', views.analytics, name='analytics'),
    path('projects/filter-<str:tag>/', views.filter, name='filter'),
]
