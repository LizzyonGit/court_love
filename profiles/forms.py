from django import forms
from .widgets import CustomClearableFileInput
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Adapted from Boutique Ado"""
    class Meta:
        model = UserProfile
        fields = ('default_phone', 'level', 'profile_image',)

    profile_image = forms.ImageField(label='Profile image', required=False,
                                     widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Customise label
        self.fields['default_phone'].label = 'Phone number'
