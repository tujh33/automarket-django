from django.db import models

# Create your models here.

class Autos(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Наименование')
    year = models.CharField(max_length=100, null=True, verbose_name='Год выпуска')
    price = models.DecimalField(verbose_name='Цена', null=True, max_length=100, max_digits=20, decimal_places=0)
    city = models.CharField(verbose_name='Город', null=True, max_length=100)
    engine = models.CharField(max_length=100, verbose_name='Двигатель')
    power = models.CharField(max_length=100, verbose_name='Мощность')
    mileage = models.CharField(max_length=100, verbose_name='Пробег')
    color = models.ForeignKey('Colors', on_delete=models.PROTECT, null=True, verbose_name='Цвет')
    gear = models.ForeignKey('Gears', on_delete=models.PROTECT, null=True, verbose_name='Привод')
    transmission = models.ForeignKey('Transmissions', on_delete=models.PROTECT, null=True, verbose_name='Трансмиссия')
    bodytype = models.ForeignKey('Bodytypes', on_delete=models.PROTECT, null=True, verbose_name='Тип кузова')
    rudder = models.ForeignKey('Rudders', on_delete=models.PROTECT, null=True, verbose_name='Руль')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Colors(models.Model):
    color = models.CharField(max_length=100, verbose_name='Цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Gears(models.Model):
    gear = models.CharField(max_length=100, verbose_name='Привод')

    def __str__(self):
        return self.gear

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Привода'

class Transmissions(models.Model):
    transmission = models.CharField(max_length=100, verbose_name='Трансмиссия')

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссии'

class Bodytypes(models.Model):
    bodytype = models.CharField(max_length=100, verbose_name='Тип кузова')

    def __str__(self):
        return self.bodytype

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузова'

class Rudders(models.Model):
    rudder = models.CharField(max_length=100, verbose_name='Руль')

    def __str__(self):
        return self.rudder

    class Meta:
        verbose_name = 'Руль'
        verbose_name_plural = 'Рули'