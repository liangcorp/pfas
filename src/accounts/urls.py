from django.urls import path

from . import views
from .views import (
               CustomLogoutView,
               CustomPasswordResetView,
               CustomPasswordResetDoneView,
               CustomPasswordResetConfirmView,
               CustomPasswordResetCompleteView
               )

app_name = "accounts"

urlpatterns = [
    path('', views.login_user, name='login'),

    path('login/', views.login_user, name='login'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('password_change/', views.password_change, name='password_change'),

    path('password_reset/',
         CustomPasswordResetView.as_view(),
         name='password_reset'),

    path('password_reset/done/',
         CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path(r'password_reset_confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path(r'password_reset_complete/',
         CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('register/', views.register, name='register'),

]
