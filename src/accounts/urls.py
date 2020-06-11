from django.urls import path

from . import views
from .views import (
               AccountsLoginView,
               AccountsLogoutView
               )
app_name = "accounts"

urlpatterns = [
    path('', AccountsLoginView.as_view(), name='accounts'),

    path('login/', AccountsLoginView.as_view(), name='login'),
    path('logout/', AccountsLogoutView.as_view(), name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/',
         views.password_change_done,
         name='password_change_done'),

    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/',
         views.password_reset_done,
         name='password_reset_done'),

    path('reset/', views.reset, name='reset'),
    path('reset/done/', views.reset_done, name='reset_done'),
    path('register', views.register, name='register'),
    path('profile/', views.redirect_to_app, name='profile'),
]
