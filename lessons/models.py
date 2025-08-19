from django.db import models

# Set image choices

BERNARDO = 'bernardo.webp'
MARINA = 'marina.webp'
ABEL = 'abel.webp'
SERVE = 'serve.webp'
ATTACK = 'attack.webp'
GENERAL = 'general.webp'

IMAGE_CHOICES = (
    (GENERAL, 'general'),
    (SERVE, 'serve'),
    (BERNARDO, 'Bernardo'),
    (MARINA, 'Marina'),
    (ABEL, 'Abel'),
    (ATTACK, 'attack'),
)

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
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    date_time = models.DateTimeField()
    duration = models.ForeignKey('Duration', null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="lessons")
    capacity = models.ForeignKey('Capacity', null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="lessons")
    places_left = models.PositiveIntegerField(null=True, blank=True)
    level_interval = models.ForeignKey('Level', null=True,
                                       on_delete=models.SET_NULL,
                                       related_name="lessons")
    place = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL,
                              related_name="lessons")
    deleted = models.BooleanField(default=False)
    image = models.CharField(max_length=255, choices=IMAGE_CHOICES,
                             null=True, blank=True)

    class Meta:
        """Order from earliest to later"""
        ordering = ['date_time']

    def __str__(self):
        return self.name

    # Via https://stackoverflow.com/questions/4380879/django-model-field-default-based-off-another-field-in-same-model
    # If not set, but not 0, set it to same as capacity value.
    def save(self, *args, **kwargs):
        if self.places_left is None:
            self.places_left = self.capacity.capacity
        super(Lesson, self).save(*args, **kwargs)


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
