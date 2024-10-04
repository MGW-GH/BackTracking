from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Stamp, Rating
from .forms import RatingForm, StampForm


class StampList(generic.ListView):
    queryset = Stamp.objects.all()
    template_name = "blog/stamp_feed.html"
    paginate_by = 8


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

    user_has_rated = False
    if request.user.is_authenticated:
        user_has_rated = stamp.ratings.filter(user=request.user).exists()

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
            return redirect('stamp_detail', title=title)

    rating_form = RatingForm(data=request.POST)
    print("About to render template")

    return render(
        request,
        "blog/stamp_detail.html",
        {"stamp": stamp,
         "ratings": ratings,
         "rating_count": rating_count,
         "rating_form": rating_form,
         "user_has_rated": user_has_rated, },
    )


def rating_edit(request, title, rating_id):
    """
    View to edit ratings.
    """
    rating = get_object_or_404(Rating, pk=rating_id, user=request.user)

    if request.method == "POST":
        # Bind the form with the POST data and the existing rating instance
        rating_form = RatingForm(data=request.POST, instance=rating)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.approved = False
            rating.save()
            messages.success(request, 'Rating Updated!')
        else:
            messages.error(request, 'Error updating rating!')

    return HttpResponseRedirect(reverse('stamp_detail', args=[title]))


def rating_delete(request, title, rating_id):
    queryset = Stamp.objects
    stamp = get_object_or_404(queryset, title=title)
    rating = get_object_or_404(Rating, pk=rating_id)

    if rating.user == request.user:
        rating.delete()
        messages.add_message(request, messages.SUCCESS, 'Rating removed!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own ratings!')

    return HttpResponseRedirect(reverse('stamp_detail', args=[title]))


@login_required
def add_stamp(request):
    if request.method == 'POST':
        form = StampForm(request.POST, request.FILES)
        if form.is_valid():
            stamp = form.save(commit=False)
            stamp.user = request.user
            stamp.save()
            return redirect('feed')
    else:
        form = StampForm()
    return render(request, 'blog/add_stamp.html', {'form': form})


def edit_stamp(request, title):
    """
    view to edit stamps
    """
    stamp = get_object_or_404(Stamp, title=title)

    if request.method == "POST":
        form = StampForm(request.POST, request.FILES, instance=stamp)
        if form.is_valid():
            stamp = form.save(commit=False)  # Don't save yet
            stamp.user = request.user  # Assign the current user to the stamp
            stamp.save()
            messages.success(request, "Stamp updated successfully.")
            return redirect('stamp_detail', title=title)
    else:
        form = StampForm(instance=stamp)
    return render(request, 'blog/add_stamp.html', {
        'form': form, 'stamp': stamp})


def delete_stamp(request, title):
    """
    view to delete stamps
    """
    stamp = get_object_or_404(Stamp, title=title)

    if request.method == "POST":
        stamp.delete()
        messages.success(request, "Stamp deleted successfully.")
        return redirect('feed')
    return redirect('stamp_detail', title=title)


def search_results(request):
    country_initials = request.GET.get('country')
    stamps = Stamp.objects.filter(
        country=country_initials
        ) if country_initials else Stamp.objects.none()
    return render(request, 'blog/search_results.html', {
            'stamps': stamps, 'country': country_initials})
