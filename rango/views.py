# Create your views here.
from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    cat_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    message = {"categories": cat_list}
    message['pages'] = page_list
    return render(request, 'rango/index.html', message)


def category(request, cat_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=cat_name_slug)
        context_dict['cat_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')