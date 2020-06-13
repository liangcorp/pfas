from django.urls import path

from . import views
from .views import (
               RegistrationLogoutView,
               RegistrationPasswordResetView
               )

app_name = "registration"

urlpatterns = [
    path('', views.login_user, name='login'),

    path('login/', views.login_user, name='login'),
    path('logout/', RegistrationLogoutView.as_view(), name='logout'),

    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/',
         views.password_change_done,
         name='password_change_done'),

    path('password_reset/',
         RegistrationPasswordResetView.as_view(),
         name='password_reset'),

    path('password_reset/done/',
         views.password_reset_done,
         name='password_reset_done'),

    path('reset/', views.reset, name='reset'),
    path('reset/done/', views.reset_done, name='reset_done'),
    path('register/', views.register, name='register'),

]
