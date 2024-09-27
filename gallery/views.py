from django.shortcuts import render
from blog.models import Stamp  # Import Stamp model

# Create your views here.
def gallery(request):
    """
    Display the gallery of the logged-in user's images (Stamps)
    """
    # Assuming the Stamp model has a ForeignKey linking to the User
    stamps = Stamp.objects.filter(user=request.user)  # Filter stamps by the logged-in user

    return render(request, 'gallery/gallery.html', {'stamps': stamps})