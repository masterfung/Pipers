from django.db import models

# Create your models here.
from person.models import Person


class Event(models.Model):
    person = models.ManyToManyField(Person, related_name='person')

    event_id = models.CharField(max_length=15, unique=True, null=True)
    event_name = models.CharField(max_length=100, blank=True)
    event_location = models.CharField(max_length=50, blank=True)
    event_address = models.CharField(max_length=400, blank=True)
    event_address2 = models.CharField(max_length=400, blank=True)
    description = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
    event_date = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    state = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=30, blank=True)
    lat = models.FloatField(max_length=30, null=True, blank=True)
    lon = models.FloatField(max_length=30, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return "{} is held at {} on {}".format(self.event_name, self.city,
                                                self.event_date)