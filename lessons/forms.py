from django import forms
from .models import Lesson, Category


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        exclude = ('deleted',)
        # code below by 'Kriss' from https://stackoverflow.com/questions/68491041/django-forms-datetimeinput-widgets-instace-value
        widgets = {
            'date_time': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'),
                                             attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded'
