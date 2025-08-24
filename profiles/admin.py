from django.contrib import admin
from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Specifies which fields are in list display
    """
    list_display = ['user', 'level', 'default_phone', ]
