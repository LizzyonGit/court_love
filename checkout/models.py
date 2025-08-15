import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from lessons.models import Lesson
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.grand_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    # Added for admin reasons, easier to change level for teacher
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='ordered_lessons')
    # NULL on delete so site admin can see who ordered a deleted lesson
    lesson = models.ForeignKey(Lesson, null=False, blank=False,
                               on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False,
                                           blank=False, default=1)  # should be 1
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2, null=False,
                                         blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        In the MVP, quantity is always 1, but it is still calculated.
        """
        self.lineitem_total = self.lesson.price * self.quantity

        super().save(*args, **kwargs)

    def __str__(self):
        """Return lesson id and order nr"""
        return f' {self.lesson.pk} on order {self.order.order_number}'
