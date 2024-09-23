from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewPost
from .models import Rating

# Register your models here.
admin.site.register(NewPost)
admin.site.register(Rating)