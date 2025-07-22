from django.shortcuts import render, redirect, reverse
from .models import Lesson, Category, Place
from .forms import LessonForm

from django.contrib import messages

# Create your views here.


def all_lessons(request):
    """
    A view to show all lessons,
    sorting and categories
    """

    lessons = Lesson.objects.all()

    categories = None  # if not set to None, error
    places = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            lessons = lessons.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'place' in request.GET:
            places = request.GET['place'].split(',')
            lessons = lessons.filter(place__place__in=places)
            places = Place.objects.filter(place__in=places)

    context = {
        'lessons': lessons,
        'current_categories': categories,
        'current_places': places,
    }

    return render(request, 'lessons/lessons.html', context)


def add_lesson(request):
    """Add lesson to website"""
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added lesson')
            return redirect(reverse('add_lesson'))
        else:
            messages.error(request,
                           'Failed to add lesson. Ensure the form is valid.')
    else:
        form = LessonForm()
    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
