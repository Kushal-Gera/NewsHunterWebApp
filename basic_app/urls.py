from django.urls import path, include
from basic_app import views


app_name = "basic_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/" + "<int:id>/", views.detail, name="detail"),
]
