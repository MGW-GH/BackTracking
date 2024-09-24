from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Stamp
from .models import Rating
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Stamp)
class StampAdmin(SummernoteModelAdmin):

    list_display = ('title', 'country', 'user')
    search_fields = ['title']
    list_filter = ('country',)
    prepopulated_fields = {'location': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Rating)