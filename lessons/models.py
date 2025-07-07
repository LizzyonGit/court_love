from django.db import models

# Create your models here.


class Category(models.Model):
    """Category model copied from Boutique Ado"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Lesson(models.Model):
    """Store the lesson product"""
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="lessons")
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    date_time = models.DateTimeField()
    duration = models.ForeignKey('Duration', null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="lessons")
    capacity = models.ForeignKey('Capacity', null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="lessons")
    level_interval = models.ForeignKey('Level', null=True,
                                       on_delete=models.SET_NULL,
                                       related_name="lessons")
    place = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL,
                              related_name="lessons")

    #image_url = models.URLField(max_length=1024, null=True, blank=True)
    #image = models.ImageField(null=True, blank=True)

    class Meta:
        """Order from earliest to later"""
        ordering = ['date_time']

    def __str__(self):
        return self.name


class Duration(models.Model):
    """
    Stores a duration time.
    """
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.duration


class Capacity(models.Model):
    """
    Stores a capacity number.
    """
    class Meta:
        verbose_name_plural = 'Capacities'

    capacity = models.PositiveIntegerField()

    def __str__(self):
        """returns only the nr in admin"""
        return str(self.capacity)


class Level(models.Model):
    """
    Stores a level interval.
    """
    level = models.CharField(max_length=254)

    def __str__(self):
        return self.level


class Place(models.Model):
    """
    Stores a place where the lesson is.
    """
    place = models.CharField(max_length=254)

    def __str__(self):
        return self.place
