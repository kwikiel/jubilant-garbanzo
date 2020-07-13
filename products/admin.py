from django.contrib import admin

# Register your models here.
# Why there is a dot
from .models import Product

admin.site.register(Product)