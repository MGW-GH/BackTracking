from django.contrib import admin
from .models import User_profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(User_profile)
class User_profileAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)