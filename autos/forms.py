from django import forms
from .models import *


class AutosForm(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Наименование'}))
    year = forms.CharField(max_length=100, label='Год выпуска', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Год выпуска'}))
    price = forms.DecimalField(label='Цена', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Цена'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Город'}))
    engine = forms.CharField(label='Двигатель', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Двигатель'}))
    power = forms.CharField(label='Мощность (л.с)', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Мощность (л.с)'}))
    mileage = forms.CharField(label='Пробег, в км', widget=forms.TextInput(attrs={'class': "auto_post_input",'placeholder': 'Пробег, в км'}))
    color = forms.ModelChoiceField(queryset=Colors.objects.all(), label='Цвет', empty_label='Цвет', widget=forms.Select(attrs={'class':'auto_post_input auto_post_select'}))
    gear = forms.ModelChoiceField(queryset=Gears.objects.all(), label='Привод', empty_label='Привод', widget=forms.Select(attrs={'class':'auto_post_input auto_post_select'}))
    transmission = forms.ModelChoiceField(queryset=Transmissions.objects.all(), label='Трансмиссия', empty_label='Трансмиссия', widget=forms.Select(attrs={'class':'auto_post_input auto_post_select'}))
    bodytype = forms.ModelChoiceField(queryset=Bodytypes.objects.all(), label='Тип кузова', empty_label='Кузов', widget=forms.Select(attrs={'class':'auto_post_input auto_post_select'}))
    rudder = forms.ModelChoiceField(queryset=Rudders.objects.all(), label='Руль', empty_label='Руль', widget=forms.Select(attrs={'class':'auto_post_input auto_post_select'}))