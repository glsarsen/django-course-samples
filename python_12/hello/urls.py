from django.urls import path
from . import views

# www.site.com/  -   ""
# www.site.com/admin/  -   "admin/"
# www.site.com/article/  -   "article/"


urlpatterns = [
    path("", views.index),
    path("dow", views.day_of_the_week)
]
