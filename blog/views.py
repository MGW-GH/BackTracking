from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Stamp
from .forms import RatingForm

# Create your views here.
class StampList(generic.ListView):
    queryset = Stamp.objects.all()
    template_name = "blog/stamp_feed.html"
    paginate_by = 6


def stamp_detail(request, title):
    """
    Display an individual :model:`blog.Stamp`.

    **Context**

    ``stamp``
        An instance of :model:`blog.Stamp`.

    **Template:**

    :template:`blog/stamp_detail.html`
    """

    queryset = Stamp.objects
    stamp = get_object_or_404(queryset, title=title)
    ratings = stamp.ratings.all().order_by("-created_at")
    rating_count = stamp.ratings.filter(approved=True).count()

    if request.method == "POST":
        rating_form = RatingForm(data=request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.stamp = stamp
            rating.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Rating submitted'
            )

    rating_form = RatingForm()

    return render(
        request,
        "blog/stamp_detail.html",
        {"stamp": stamp,
        "ratings": ratings,
        "rating_count": rating_count,
        "rating_form": rating_form,
        },
    )

