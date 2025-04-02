from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe



def snkr_index(request):
    shoes = Shoe.objects.all() 
    return render(request, 'shoes/index.html', {'shoes': shoes})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snkr_detail(request, snkr_id):
    shoe = Shoe.objects.get(id=snkr_id)
    print(shoe)
    return render(request, 'shoes/detail.html', {'shoe': shoe})

class SnkrCreate(CreateView):
    model = Shoe
    fields = '__all__'

class SnkrUpdate(UpdateView):
    model = Shoe
    fields = ['amount', 'description', 'image']

class SnkrDelete(DeleteView):
    model = Shoe
    success_url = '/snkrs/'
