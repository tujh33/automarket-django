# Generated by Django 3.2.8 on 2021-10-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_autos_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autos',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='autos',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=10, max_length=100, null=True, verbose_name='Цена'),
        ),
    ]
