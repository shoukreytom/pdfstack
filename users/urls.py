from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
