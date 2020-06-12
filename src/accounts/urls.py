from django.urls import path

from . import views
from .views import (
               AccountsLogoutView,
               )

app_name = "accounts"

urlpatterns = [
    path('', views.login_user, name='login'),

    path('login/', views.login_user, name='login'),
    path('logout/', AccountsLogoutView.as_view(), name='logout'),

    # TODO Switch function views to class views.
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

    # TODO remove the redirect in the future
    path('profile/', views.redirect_to_app, name='profile'),
]
