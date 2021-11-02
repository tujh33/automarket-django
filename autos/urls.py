from django.urls import path

from autos.views import *

urlpatterns = [
    path('', index, name ='home'),
    path('auto/<int:auto_id>/', get_detail_auto_info, name='detail_auto_info'),
    path('add_post/', add_post, name='add_post')
]