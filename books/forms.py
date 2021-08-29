from django import forms

from .models import Book


class UploadBookForm(forms.ModelForm):
    book = forms.FileField(label='', widget=forms.FileInput(attrs={
        'accept': 'application/pdf',
        'name': 'pdf_file',
    }))

    class Meta:
        model = Book
        fields = ['book']
