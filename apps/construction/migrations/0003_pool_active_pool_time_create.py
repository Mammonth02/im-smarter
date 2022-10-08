# Generated by Django 4.1.1 on 2022-10-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AddField(
            model_name='pool',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]