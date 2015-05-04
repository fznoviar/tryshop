from django.contrib import admin

from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
    '''
        Admin View for Page
    '''
    list_display = ('name', 'active')

class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('name', 'slug', 'active')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)
