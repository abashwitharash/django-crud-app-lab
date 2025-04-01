from django.shortcuts import render
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


