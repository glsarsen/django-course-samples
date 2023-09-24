from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addphone/", views.add_phone, name="addphone"),
    path("viewcontacts/", views.view_contacts, name="viewcontacts"),
    path("searchcontacts/", views.search_contacts, name="searchcontacts"),
]
