__author__ = 'thibaut'

from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}


@register.simple_tag
def active(request, pattern):
    import re

    pattern = "^%s$" % pattern
    if re.search(pattern, request.path):
        return 'active'
    return ''