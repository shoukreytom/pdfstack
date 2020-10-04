from django import forms

from .models import Book


class UploadBook(forms.ModelForm):
    book = forms.FileField(label='')

    class Meta:
        model = Book
        fields = ['book']
