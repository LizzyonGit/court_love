import django_filters
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Lesson


class DateFilter(django_filters.FilterSet):
    date_time = DateFromToRangeFilter(field_name='date_time', label='Filter by Date Range:',
                                        widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Lesson
        fields = ['date_time']
