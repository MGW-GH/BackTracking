from django.contrib import admin
from .models import User_profile
from django_summernote.admin import SummernoteModelAdmin
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken


@admin.register(User_profile)
class User_profileAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)


# Unregister the allauth models from admin
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)