from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


urlpatterns = [
    path('', manage_items, name="items"),
    path('single/<slug:key>', manage_item, name="single_item"),
    path('api2/' , get_items, name="get_items")
]
urlpatterns = format_suffix_patterns(urlpatterns)
