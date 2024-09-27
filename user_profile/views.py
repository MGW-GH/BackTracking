from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User_profile


def user_profile(request):
    """
    Renders the About page
    """
    user_profile = User_profile.objects.get(user=request.user) 

    return render(
        request,
        "user_profile/user_profile.html",
        {"user_profile": user_profile},
    )