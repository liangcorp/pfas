from django.urls import path

from . import views

app_name = "landing"

urlpatterns = [
    path('', views.get_landing_page, name='index'),
]
