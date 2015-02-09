from autoslug.settings import slugify
from django.contrib import admin

# Register your models here.
from rango.models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'category']
    list_display = ['title', 'url', 'category']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)