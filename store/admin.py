from django.contrib import admin
from .models import Product
from store import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_id', 'price','stock', 'category',  'created_date', 'modified_date', 'is_available'] # Fields to display in the list view
    list_filter = ['created_date', 'modified_date'] # Filters to display in the right sidebar
    search_fields = ['product_name', 'description', 'product_id'] # Fields to search for products
    prepopulated_fields = {'slug': ('product_name',)} # Automatically create a slug field from the name field

admin.site.register(Product, ProductAdmin)
