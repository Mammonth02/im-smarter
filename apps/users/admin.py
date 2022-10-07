from django.contrib import admin

from apps.users.models import Basket, Order, User

# Register your models here.

admin.site.register(User)
admin.site.register(Basket)
admin.site.register(Order)