
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.shop.models import Product

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Аватарка')
    phone = models.IntegerField(null=True, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name= 'Пользователь'

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество', null=True)
    status = models.BooleanField(default=False, verbose_name='Заказ')


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.product}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    basket = models.ManyToManyField(Basket)
    time_create = models.DateTimeField(auto_now_add=True)