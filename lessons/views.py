from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Lesson, Category, Place
from .forms import LessonForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def add_lesson(request):
    """Add lesson to website"""
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised.')
        return redirect(reverse('home'))

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


@login_required
def edit_lesson(request, lesson_id):
    """ Edit a lesson on the website"""
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated lesson.')
            return redirect(reverse('lessons'))
        else:
            messages.error(
                request, 'Failed to update lesson. Ensure the form is valid.')
    else:
        form = LessonForm(instance=lesson)
        messages.info(request, f'You are editing {lesson.name}')

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)


@login_required
def delete_lesson(request, lesson_id):
    """ Delete a lesson from the website"""
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.delete()
    messages.success(request, 'Lesson deleted.')
    return redirect(reverse('lessons'))
