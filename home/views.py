from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Stamp
from .forms import CountrySearchForm

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'


def home(request):
    form = CountrySearchForm()
    stamps = Stamp.objects.all()  # Get all stamps initially

    # Check if a country has been selected
    if request.method == 'GET':
        selected_country = request.GET.get('country', None)
        if selected_country:
            stamps = stamps.filter(country=selected_country)  # Filter stamps by selected country

    return render(request, 'home.html', {'form': form, 'stamps': stamps})