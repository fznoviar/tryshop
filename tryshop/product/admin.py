from django.contrib import admin

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('title', 'short_description', 'price')

class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('title', 'slug', 'active')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
