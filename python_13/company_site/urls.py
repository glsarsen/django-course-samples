from django.urls import path
from . import views


app_name="c_site"
urlpatterns = [
    path('branches/<str:name>/', views.branches, name="branches"),
    path('branches/<path:name>/', views.branches, name="branches"),
    path('branches/', views.branches, name="branches"),
    path('news/<path:aftertext>', views.news, name="news"),
    path('news/', views.news, name="news"),
    path('management/<path:aftertext>', views.management, name="management"),
    path('management/', views.management, name="management"),
    path('about/<path:aftertext>', views.about, name="about_page"),
    path('about/', views.about, name="about_page"),
    path('contacts/<path:aftertext>', views.contacts, name="contacts"),
    path('contacts/', views.contacts, name="contacts"),
    path('', views.index, name="index"),
    path('<path:aftertext>', views.index, name="index"),
]
