from django.contrib import admin
from .models import Listing, Category, Tags, Review

# Register your models here.

admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Review)