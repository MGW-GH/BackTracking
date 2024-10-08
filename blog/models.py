from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url
from django_countries.fields import CountryField
from django.contrib.auth.models import User


STATUS = ((0, "Current location"), (1, "Past adventure"))


# Create models here.
class Stamp(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_stamps", null=True)
    country = CountryField(max_length=200)
    location = models.CharField(max_length=100, unique=False)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_webp_image(self):
        url, options = cloudinary_url(self.image.public_id, format="webp", quality="auto:low")
        return url

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} by {self.user}"


class Rating(models.Model):
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rater")
    percentage_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        # Ensure that the score is always between 0 and 100
        if 0 <= self.percentage_score <= 100:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Score must be between 0 and 100")

    def __str__(self):
        return f"{self.user} scored this stamp {self.percentage_score}!"
