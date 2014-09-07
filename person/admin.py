from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from person.forms import ProfileCreationForm
from person.models import Person


class PersonAdmin(UserAdmin):
    add_form = ProfileCreationForm

    def get_fieldsets(self, request, obj=None):  # 4c (whole method)
        """
        Get the custom fields that are missing from the usercreationform for the PatronAdmin

        """

        return self.fieldsets + (
            ('Custom Fields', {'fields': ('user_type', 'phone'
            )}),
        )

    list_display = ['username', 'user_type']
    search_fields = ['user_type', 'phone']

admin.site.register(Person, PersonAdmin)