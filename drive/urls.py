from django.urls import path
from . import views

app_name = "drive"

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>/", views.delete_photo, name="delete"),
]