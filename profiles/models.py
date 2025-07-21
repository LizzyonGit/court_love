from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Level 1.5 - 7
LEVEL = [(i/2, i/2) for i in range(3, 15, 1)]

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    personal information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    level = models.DecimalField(choices=LEVEL, decimal_places=1, max_digits=4, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
