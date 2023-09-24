from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thank_you/", views.second_page, name="thank_you_page")
]
