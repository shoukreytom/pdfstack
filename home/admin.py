from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_filter = ['owner', ]


admin.site.register(Book, BookAdmin)
