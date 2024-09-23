from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

STATUS = ((0, "Current location"), (1, "Past adventure"))

# Create your models here.
class NewPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", null=True)
    country = CountryField(max_length=200)
    location = models.CharField(max_length=100, unique=False)
    image = models.ImageField(upload_to='media/blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


