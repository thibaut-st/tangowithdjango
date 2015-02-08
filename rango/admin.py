from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'category']
    list_display = ['title', 'url', 'category']

admin.site.register(Category)
admin.site.register(Page, PageAdmin)