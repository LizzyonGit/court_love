from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Adapted from Boutique Ado"""
    class Meta:
        model = UserProfile
        fields = ('default_phone', 'level',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Customise label
        self.fields['default_phone'].label = 'Phone number'

        placeholders = {
            'default_phone': 'Phone number',
            'level': 'Level',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded'
