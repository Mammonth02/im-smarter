from django.db import models

from apps.users.models import User

# Create your models here.

class ServiceType(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    desctiption = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='service/', verbose_name='Фото', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Типы услуги'
        verbose_name= 'Тип услуги'

class Service(models.Model):
    CHOOS = (
        (True, 'По расписанию'),
        (False, "Один раз"),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Заказчик')
    category = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True, verbose_name='Катигория')
    message = models.TextField(verbose_name='Коментарий')
    active = models.BooleanField(default=False, verbose_name='Активность')
    time_create = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return f'{self.user}-{self.category}'

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name= 'Услуга'

