from django.shortcuts import render
from .models import Lesson, Category, Place
from .filters import DateFilter
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


def filter_date(request):
    lessons = Lesson.objects.all()
    date_filter = DateFilter(request.GET, queryset=lessons)
    lessons = date_filter.qs

    context = {
        "filtered_lessons": lessons,
        "date_filter": date_filter,
        }

    return render(request, "lessons/filter.html", context)
