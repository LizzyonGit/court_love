from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# from Boutiqe Ado
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove current profile image after Update')
    initial_text = _('Select an image and click Update below')
    input_text = _('')
    template_name = (
        'profiles/custom_widget_templates/custom_clearable_file_input.html')
