from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_lessons, name='lessons'),
    path('add/', views.add_lesson, name='add_lesson'),
]
