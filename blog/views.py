from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Stamp

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

    queryset = Post.objects.filter(status=1)
    stamp = get_object_or_404(queryset, title=title)

    return render(
        request,
        "blog/stamp_detail.html",
        {"stamp": stamp},
    )