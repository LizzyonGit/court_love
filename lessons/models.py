from django.db import models

# Create your models here.


class Category(models.Model):
    """Category model copied from Boutique Ado"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Lesson(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    date_time = models.DateTimeField()
    duration = models.IntegerField(choices=, default=)# check movie project because i want this to be created in admin
    capacity = models.PositiveIntegerField() #needs to reduce when ordered, how?
    level = models.IntegerField(choices=, default=)# check movie project because i want this to be created in admin
    place = models.IntegerField(choices=, default=)# check movie project because i want this to be created in admin

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
