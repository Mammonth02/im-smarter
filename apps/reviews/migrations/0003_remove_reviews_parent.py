# Generated by Django 4.1.1 on 2022-10-10 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
    ]