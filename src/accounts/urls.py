from django.urls import path, re_path

from . import views
from .views import (
    CutomeSignupView,
    CustomConfirmEmailView,
    CustomPasswordChangeView,
    CustomPasswordResetView,
    CustomEmailView,
    CustomPasswordResetDoneView
)

app_name = "accounts"

urlpatterns = [
    path('', views.login_user, name='account_login'),

    path('login/', views.login_user, name='account_login'),

    path('logout/', views.logout_user, name='logout'),

    path("password/change/", CustomPasswordChangeView.as_view(),
         name="account_change_password"),
    # path("password/set/", views.password_set, name="account_set_password"),
    # path("inactive/", views.account_inactive, name="account_inactive"),

    # E-mail
    path("email/", CustomEmailView.as_view(), name="account_email"),
    path("confirm-email/", views.confirm_email_sent,
         name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$",
            CustomConfirmEmailView.as_view(), name="account_confirm_email"),

    # password reset
    path("password/reset/", CustomPasswordResetView.as_view(),
         name="account_reset_password"),

    path("password/reset/done/", CustomPasswordResetDoneView.as_view(),
         name="account_reset_password_done"),

    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            views.password_reset_from_key,
            name="account_reset_password_from_key"),

    path("password/reset/key/done/", views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),

    path('signup/', CutomeSignupView.as_view(), name='account_signup'),

]
