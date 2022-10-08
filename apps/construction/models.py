from types import ModuleType
from unicodedata import category
from django.db import models

from apps.users.models import User

class PoolCat(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    desctiption = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='pool_cat/', verbose_name='Фото')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Вид бассейна'
        verbose_name= 'Виды бассейна'

class Decoration(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='decoration/', verbose_name='Фото')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Отделка'
        verbose_name_plural = 'Отделка'

class Additionally(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Дополнительно'
        verbose_name= 'Дополнительно'

class Pool(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Заказчик')
    category = models.ForeignKey(PoolCat, on_delete=models.SET_NULL, null=True, verbose_name='Катигория')
    width = models.FloatField(verbose_name='Ширина')
    length = models.FloatField(verbose_name='Длина')
    depth = models.FloatField(verbose_name='Глубина')
    decoration = models.ForeignKey(Decoration, on_delete=models.SET_NULL, null=True, verbose_name='Отделка')
    additionally = models.ManyToManyField(Additionally, verbose_name='Дополнительно')
    desctiption = models.TextField(verbose_name='Коментарий')
    active = models.BooleanField(default=False, verbose_name='Активность')
    time_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name= 'Заказ'
