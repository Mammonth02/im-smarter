from django import template

from apps.home_site.models import SiteInfo
from apps.shop.models import Category


register = template.Library()

@register.simple_tag()
def info():
    if SiteInfo.objects.all():
        for i in SiteInfo.objects.all():
            site = i
        return site

@register.simple_tag()
def shop_cat():
    shop = Category.objects.all()
    return shop


