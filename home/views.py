from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import FileResponse, HttpResponse, Http404
from django.urls import reverse_lazy
import os

from .models import Book
from .forms import UploadBook


def home(request):
    return render(request, 'home/index.html')


class BookList(LoginRequiredMixin, View):
    init_form = UploadBook()

    def get(self, request):
        books = Book.objects.filter(owner=request.user)
        return render(request, 'home/books.html', {
            'form': self.init_form,
            'books': books
        })

    def post(self, request):
        form = UploadBook(request.POST, request.FILES)
        if form.is_valid():
            book_name = form.cleaned_data.get('book')
            if str(book_name).lower().endswith('pdf'):
                obj = form.save(commit=False)
                obj.owner = request.user
                obj.save()
                messages.success(
                    request, "Your file has been uploaded successfully!!!")
            else:
                messages.error(
                    request, "You should select pdf file (e.g: exampl.pdf).")
            books = Book.objects.filter(owner=request.user)
        else:
            messages.error(
                request, "Sorry!! you didn't select anything.")
        return render(request, 'home/books.html', {
            'form': self.init_form,
            'books': books
        })


def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return FileResponse(book.book.open(), content_type='application/pdf')


def read_book(request, pk, file_=None):
    book = get_object_or_404(Book, pk=pk)
    response = FileResponse(book.book.open(), content_type='application/pdf')
    book_file = open(book.book.path)
    print(dir(book_file))
    cred_id = os.environ.get('CRED_ID')     # credentail_id for adobe reader
    return render(request, 'home/viewer.html', {'book': book_file})


class DeleteBook(DeleteView):
    model = Book
    template_name = 'home/confirm_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('home:books')
