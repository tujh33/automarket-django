from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from .models import Autos
from .forms import AutosForm

def index(request):
    auto = Autos.objects.all().order_by('-created_at')
    context = {
        "data":"data",
        "autos":auto,
    }
    return render(request,'autos/index.html', context)


def get_detail_auto_info(request, auto_id):
    # auto_info = Autos.objects.get(pk = auto_id)
    auto_info = get_object_or_404(Autos,pk = auto_id)
    context = {
        "auto_info":auto_info
    }
    return render(request, 'autos/detail_card_auto.html', context)

def add_post(request):
    if request.method == 'POST':
        form = AutosForm(request.POST)
        if form.is_valid():
            Autos.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = AutosForm()
    return render(request, 'autos/add_post.html', {'form':form})