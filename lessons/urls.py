from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_lessons, name='lessons'),
    path('/filter', views.filter_date, name="filter_date"),
]
