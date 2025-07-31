from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Lesson, Category, Place
from .forms import LessonForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils import timezone

# Create your views here.


def all_lessons(request):
    """
    A view to show all future lessons,
    sorting and categories
    """
    # lessons with future date
    lessons = Lesson.objects.filter(date_time__gt=timezone.now())

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
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            # info message if places left is higher than capacity
            if form.cleaned_data['places_left'] > form.cleaned_data['capacity'].capacity:
                messages.info(request,
                              'Note that places left is more than the lesson capacity.')
            # info message if date has passed
            if form.cleaned_data['date_time'] <= timezone.now():
                messages.info(request,
                              "The lesson's date has passed, the lesson will not be displayed but is visible in admin.")
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
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            # info message if places left is higher than capacity
            if form.cleaned_data['places_left'] > form.cleaned_data['capacity'].capacity:
                messages.info(request,
                              'Note that places left is more than the lesson capacity.')
            # info message if date has passed
            if form.cleaned_data['date_time'] <= timezone.now():
                messages.info(request,
                              "The lesson's date has passed, the lesson will not be displayed but is visible in admin.")
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
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.delete()
    messages.success(request, 'Lesson deleted.')
    return redirect(reverse('lessons'))
