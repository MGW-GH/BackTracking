from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Stamp
from .models import Rating

# Register your models here.
admin.site.register(Stamp)
admin.site.register(Rating)