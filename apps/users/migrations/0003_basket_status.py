# Generated by Django 4.1.1 on 2022-10-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Заказ'),
        ),
    ]