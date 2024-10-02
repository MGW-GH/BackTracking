from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.StampList.as_view(), name='feed'),
    path('add-stamp/', views.add_stamp, name='add_stamp'),
    path('search/', views.search_results, name='search_results'),
    path('<str:title>/', views.stamp_detail, name='stamp_detail'),
    path('stamp/<str:title>/edit/', views.edit_stamp, name='edit_stamp'),
    path('<str:title>/edit_rating/<int:rating_id>', views.rating_edit, name='rating_edit'),
    path('<str:title>/delete_rating/<int:rating_id>', views.rating_delete, name='rating_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)