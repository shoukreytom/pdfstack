from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'books'

urlpatterns = [
	path('',  views.BookList.as_view(), name='list'),
    path('upload/',  views.UploadBook.as_view(), name='upload'),
    path('<int:pk>/delete/', views.DeleteBook.as_view(), name='delete'),
    path('<int:pk>/download/', views.download_book, name='download'),
    path('<int:pk>/read/', views.read_book, name='read'),
    path('pdf/viewer.html/', views.view_book, name='view-book'),
]
