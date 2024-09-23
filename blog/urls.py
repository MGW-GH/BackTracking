from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_blog, name='blog'),
]