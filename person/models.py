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

    NOT_ATTENDING = 'Not Attending'
    ATTENDING = 'Attending'

    BUSY = (
        (NOT_ATTENDING, 'Not Attending'),
        (ATTENDING, 'Attending')
    )


    user_type = models.CharField(max_length=15, choices=TYPE, default=ATTENDEE)
    phone = models.CharField(max_length=12, blank=True)
    user_event_status = models.CharField(choices=BUSY, max_length=15, default=NOT_ATTENDING)

    def __unicode__(self):
        return self.first_name