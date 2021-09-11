from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .forms import AddUserForm, UpdateUserForm
from .models import User, Profile, EmailAddress


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ("email", "password")


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        fields = ("user", "image")


class EmailResource(resources.ModelResource):
    class Meta:
        model = EmailAddress
        fields = ("email", "is_verified")


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    add_form = AddUserForm
    form = UpdateUserForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource


class EmailAddressAdmin(ImportExportModelAdmin):
    resource_class = EmailResource


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)