from django.shortcuts import render
from django.http import *
from .models import Autos
from .forms import AutosForm

def index(request):
    auto = Autos.objects.all()
    context = {
        "data":"data",
        "autos":auto,
    }
    return render(request,'autos/index.html', context)


def get_detail_auto_info(request, auto_id):
    auto_info = Autos.objects.get(pk = auto_id)
    context = {
        "auto_info":auto_info
    }
    return render(request, 'autos/detail_card_auto.html', context)

def add_post(request):
    if request.method == 'POST':
        pass
    else:
        form = AutosForm()
    return render(request, 'autos/add_post.html', {'form':form})