from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from person.models import Person
from person.serializer import PersonSerializer


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


class PersonMixin(object):
    """
    This EventMixin is used for Bond's events.
    This code is recycled across different classes. It makes
    the most sense to abstract this out and use a mixin, as
    shown here.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(PersonMixin, generics.ListCreateAPIView):
    """
    List all events in the DB, or allows the
    users to create new events.
    """
    permission_classes = (IsAuthenticated,)


class PersonDetail(PersonMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)