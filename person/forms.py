from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from person.models import Person

__author__ = '@masterfung'


class ProfileCreationForm(UserCreationForm):  # 4b (whole class / module)
    '''
   A form that we can use to create a patron with no privileges

   Use this form to create user simply by admin settings through the use of username & password
   '''
    # Thanks to http://stackoverflow.com/questions/16953302/ for the solution to this one
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Person._default_manager.get(username=username)
        except Person.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()