from django.urls import path
from . import views

urlpatterns = [
    path('mission/', views.mission_view, name='mission'),
    path('vision/', views.vision_view, name='vision'),
    path('objectives/', views.objectives_view, name='objectives'),
]