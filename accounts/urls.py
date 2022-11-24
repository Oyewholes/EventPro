from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns=[
    re_path(r'^login$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'signup/$', views.SignUp.as_view(), name='signup'),
    re_path('reset_password/',
            auth_views.PasswordResetView.as_view(template_name ="accounts/password_reset.html"),
            name='reset_password'),
    re_path('reset_password_sent/',
            auth_views.PasswordResetDoneView.as_view(template_name ="accounts/password_reset_sent.html"),
            name = 'password_reset_done'),
    re_path('reset/<uidb64/<token>/>',
            auth_views.PasswordResetConfirmView.as_view(template_name ="accounts/password_reset_form.html"),
            name = 'password_reset_confirm'),
    re_path('reset_password_complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name ="accounts/password_reset_done.html"),
            name='password_reset_complete')
]