from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Person(AbstractUser):
    ATTENDEE = 'Attendee'
    PLANNER = 'Planner'

    TYPE = (
        (ATTENDEE, 'Attendee'),
        (PLANNER, 'Planner')
    )

    user_type = models.CharField(max_length=15, choices=TYPE, default=ATTENDEE)
    phone = models.CharField(max_length=12, blank=True)

    def __unicode__(self):
        return self.first_name