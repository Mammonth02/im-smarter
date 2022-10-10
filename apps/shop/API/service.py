from django_filters import rest_framework as filters

from apps.shop.models import Product


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'category']