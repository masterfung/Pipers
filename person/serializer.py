from rest_framework import serializers
from person.models import Person

__author__ = '@masterfung'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'email'
        )