from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Stamp, Rating
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
        print("Received a POST request")
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

    rating_form = RatingForm(data=request.POST)
    print("About to render template")

    return render(
        request,
        "blog/stamp_detail.html",
        {"stamp": stamp,
        "ratings": ratings,
        "rating_count": rating_count,
        "rating_form": rating_form,
        },
    )


def rating_edit(request, title, rating_id):
    """
    view to edit ratings
    """
    if request.method == "POST":

        queryset = Stamp.objects
        stamp = get_object_or_404(queryset, title=title)
        rating = get_object_or_404(Rating, pk=rating_id)
        rating_form = RatingForm(data=request.POST, instance=rating)

        if rating_form.is_valid() and rating.user == request.user:
            rating = rating_form.save(commit=False)
            rating.stamp = stamp
            rating.approved = False
            rating.save()
            messages.add_message(request, messages.SUCCESS, 'Rating Updated!')
        else:
            print("Form errors:", rating_form.errors)
            print("User is:", request.user)
            print("Rating user is:", rating.user)
            messages.add_message(request, messages.ERROR, 'Error updating rating!')

    return HttpResponseRedirect(reverse('stamp_detail', args=[title]))