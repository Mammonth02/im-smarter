from django.db import models
from multiselectfield import MultiSelectField

class SiteInfo(models.Model):
    WEEK = (
        ('monday', 'Пн'),
        ('tuesday', 'Вт'),
        ('wednesday', 'Ср'),
        ('thursday', 'Чт'),
        ('friday', 'Пт'),
        ('saturday', 'Сб'),
        ('sundayВс', 'Вс')
    )
    title = models.CharField(max_length=100, verbose_name='Название сайта', null=True)
    working_time_start = models.TimeField(verbose_name='Время открытия', null=True)
    working_time_end = models.TimeField(verbose_name='Время закрытия', null=True)
    working_date = MultiSelectField(choices=WEEK, verbose_name='Рабочии дни', max_length=150,  null=True)
    adress = models.CharField(max_length=250, verbose_name='Адресс', null=True)
    email = models.EmailField(verbose_name='Емайл', null=True)
    phone = models.IntegerField(verbose_name='Телефон', null=True)
    tw_link = models.URLField(null=True, verbose_name='Ссылка на twitter')
    fe_link = models.URLField(null=True, verbose_name='Ссылка на facebook')
    in_link = models.URLField(null=True, verbose_name='Ссылка на linkedin')
    sk_link = models.URLField(null=True, verbose_name='Ссылка на skype')


    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

    def __str__(self):
        return f'Инфо сайта'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class ConstructionImages(models.Model):
    image = models.ImageField(upload_to = 'construction_images/')

