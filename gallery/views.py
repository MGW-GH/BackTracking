from django.shortcuts import render
from blog.models import Stamp


# Create your views here.
def gallery(request):
    """
    Display the gallery of the logged-in user's stamps
    """
    stamps = Stamp.objects.filter(user=request.user)
    return render(request, 'gallery/gallery.html', {'stamps': stamps})
