from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, {'page_name': ''}, name="index"),
    path("<str:page_name>/", views.index, name="index"),
]
