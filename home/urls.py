from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('my/books/', views.books, name='books'),
    path('my/books/<int:pk>/delete/',
         views.DeleteBook.as_view(), name='delete-book'),
    path('my/books/<int:pk>/download/',
         views.download_book, name='download-book'),
    path('my/books/<int:pk>/read/',
         views.read_book, name='read-book'),
]
