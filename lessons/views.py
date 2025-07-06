from django.shortcuts import render
from .models import Lesson
# Create your views here.


def all_lessons(request):
    """
    A view to show all lessons,
    sorting and categories
    """

    lessons = Lesson.objects.all()

    context = {
        'lessons': lessons,
    }
    
    return render(request, 'lessons/lessons.html', context)
