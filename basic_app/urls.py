from django.urls import path, include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.next, name="next"),
    path("settings/", views.settings, name="settings"),
]
