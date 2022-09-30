from django import template
from django.shortcuts import render

from apps.home_site.models import SiteInfo
from apps.shop.models import Category
from apps.users.models import Basket


register = template.Library()

@register.simple_tag()
def info():
    for i in SiteInfo.objects.all():
        site = i
    return site

@register.simple_tag()
def shop_cat():
    shop = Category.objects.all()
    return shop


