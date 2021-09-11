from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('email/verify/send/', views.send_verification_email, name='send-verify-email'),
    path('email/verify/confirm/', views.verify_email, name='verify-email'),
    path('password/reset/', views.password_reset, name='password-reset'),
    path('password/reset/confirm/', views.password_reset_confirm, name='password-reset-confirm'),
    path('delete/', views.delete_user, name='delete-user'),
]
