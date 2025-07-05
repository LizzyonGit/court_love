from django.contrib import admin
from .models import Lesson, Category, Duration, Capacity, Level, Place

# Register your models here.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Adds fields to table and adds filter.
    """
    list_display = ('date_time', 'category', 'capacity', 'place', 'duration')
    list_filter = ('date_time', 'category', 'capacity', 'place')


admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Place)
admin.site.register(Capacity)
admin.site.register(Duration)
