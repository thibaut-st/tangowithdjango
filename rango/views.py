# Create your views here.
from django.shortcuts import render

from rango.forms import CategoryForm, PageForm

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


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, cat_slug):

    try:
        cat = Category.objects.get(slug=cat_slug)
    except:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views=0
                page.save()
                return index(request)
    else:
        form = PageForm()
    return render(request, 'rango/add_page.html', {'form': form, 'category' : cat})


def about(request):
    return render(request, 'rango/about.html')