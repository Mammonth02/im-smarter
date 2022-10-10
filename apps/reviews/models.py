from django.db import models

from apps.users.models import User
from apps.shop.models import Product

# Create your models here

class Reviews(models.Model):
    RATING = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    )
    rating = models.IntegerField(choices=RATING, verbose_name='Рейтинг')
    text = models.TextField(verbose_name='Отзыв')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Отправитель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    time_c = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user}'
