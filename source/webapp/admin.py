from django.contrib import admin

from webapp.models import Product, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)