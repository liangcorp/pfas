from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_landing_page, name='landing'),
    # path('', views.CheckAuthApp.as_view(), name="auth"),
]
