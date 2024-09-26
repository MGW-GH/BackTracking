from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.StampList.as_view(), name='feed'),
    path('<title:title>/', views.stamp_detail, name='stamp_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)