from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AddUserForm, UpdateUserForm
from .models import User, Profile, EmailAddress


class CustomUserAdmin(UserAdmin):
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


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(EmailAddress)