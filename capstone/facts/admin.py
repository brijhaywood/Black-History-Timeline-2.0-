from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Place)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'year', 'coord_v', 'coord_h', 'is_liked', 'has_viewed', 'category')
    # prepopulated_fields = {'slug': ('title',), }