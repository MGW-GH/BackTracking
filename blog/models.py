from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.CharField(max_length=50, unique=False)
    image = models.ImageField(upload_to='media/blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


