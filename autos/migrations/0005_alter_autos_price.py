# Generated by Django 3.2.8 on 2021-10-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_auto_20211028_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20, max_length=100, null=True, verbose_name='Цена'),
        ),
    ]