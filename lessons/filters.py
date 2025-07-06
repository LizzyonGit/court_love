import django_filters
from .models import Lesson


class DateFilter(django_filters.FilterSet):
    date_time = django_filters.DateFromToRangeFilter(field_name='date_time')

    class Meta:
        model = Lesson
        fields = ['date_time']
