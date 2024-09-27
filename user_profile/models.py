from django.db import models
from blog.models import Stamp  # Importing the models from the blog app
from blog.models import Rating
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User_profile(models.Model):
    alias = models.CharField(max_length=15)
    bio = models.TextField(max_length=500)
    base_country = CountryField(max_length=200)
    base_location = models.CharField(max_length=80)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiler", null=True)