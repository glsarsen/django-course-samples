from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_num>/<str:author>/', views.index),
    path('<int:article_num>/', views.index),
    path('params/', views.params),
]

# int
# str
# slug      article-about-django
# uuid      
# path


# https://127.0.0.1:8000/test/
# https://127.0.0.1:8000/test/new

# https://127.0.0.1:8000/article/4