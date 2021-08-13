from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Place(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=32)
    description = models.TextField()
    year = models.IntegerField()
    coord_v = models.FloatField()
    coord_h = models.FloatField()
    is_liked = models.BooleanField(default=False)
    has_viewed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
