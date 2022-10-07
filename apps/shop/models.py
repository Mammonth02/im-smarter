from audioop import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe


# Create your models here.

class Category(MPTTModel):
    title = models.CharField(max_length=100, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родитель')

    class Meta:
        verbose_name = 'Катигория'
        verbose_name_plural = 'Катигории'

    def __str__(self):
        return f'{self.title}'
class Product(models.Model):
    title = models.CharField(max_length=126, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Катигория')
    content = models.TextField(verbose_name='полное описание')
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    price = models.FloatField(verbose_name='Цена')
    status = models.BooleanField(default=True, verbose_name='наличие')
    description = models.TextField(verbose_name='краткое описание', null=True)
    

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px">')
        else:
            return ''

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'
class ImagesForProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f'{self.id}'

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px">')
        else:
            return ''

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name= 'Картинка'

