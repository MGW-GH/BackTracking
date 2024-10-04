from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Stamp
from .forms import CountrySearchForm


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CountrySearchForm()
        context['form'] = form

        stamps = Stamp.objects.all()

        selected_country = self.request.GET.get('country', None)
        if selected_country:
            stamps = stamps.filter(country=selected_country)
        context['stamps'] = stamps
        return context
