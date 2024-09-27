"""
URL configuration for back_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls"), name="blog-urls"),
    path("gallery/", include("gallery.urls"), name="gallery-urls"),
    path("summernote/", include("django_summernote.urls")),
    path("user_profile/", include("user_profile.urls"), name="user_profile-urls"),
    path("", include("home.urls"), name="home-urls"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
