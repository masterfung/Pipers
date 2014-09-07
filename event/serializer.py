from rest_framework import serializers
from event.models import Event

__author__ = '@masterfung'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_id',
            'event_name',
            'event_address',
            'event_address2',
            'description',
            'event_url',
            'city',
            'state',
            'zip',
            'country',

            'event_start',
            'event_end',
            'venue_name',
            'lat',
            'lon'
        )