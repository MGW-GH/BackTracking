from django.shortcuts import render
from django.views import generic
from .models import Stamp

# Create your views here.
class StampList(generic.ListView):
    queryset = Stamp.objects.all()
    template_name = "blog/stamp_feed.html"
    paginate_by = 4