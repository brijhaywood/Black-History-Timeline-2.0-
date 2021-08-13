from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    CATEGORY_CHOICES = ('SPORTS', 'SPORTS'),('INVENTIONS', 'INVENTIONS'),('MUSIC', 'MUSIC'),('STEM', 'STEM'), ('POLITICS','POLITICS'), ('LITERATURE','LITERATURE'),('ART', 'ART'),('FASHION','FASHION'), ('EMPIRES', 'EMPIRES')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    title = models.CharField(max_length=32)
    description = models.TextField()
    year = models.IntegerField()
    coord_v = models.FloatField()
    coord_h = models.FloatField()
    is_liked = models.BooleanField(default=False)
    has_viewed = models.BooleanField(default=False)
    objects = models.Manager() 
    
    def __str__(self):
        return self.title