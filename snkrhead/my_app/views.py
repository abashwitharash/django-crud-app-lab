from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
from .forms import CleaningForm



def snkr_index(request):
    shoes = Shoe.objects.all() 
    return render(request, 'shoes/index.html', {'shoes': shoes})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snkr_detail(request, snkr_id):
    shoe = Shoe.objects.get(id=snkr_id)
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', {'shoe': shoe, 'cleaning_form': cleaning_form})

class SnkrCreate(CreateView):
    model = Shoe
    fields = '__all__'

class SnkrUpdate(UpdateView):
    model = Shoe
    fields = ['amount', 'description', 'image']

class SnkrDelete(DeleteView):
    model = Shoe
    success_url = '/snkrs/'

def add_cleaning(request, snkr_id):
    # create a ModelForm instance using the data in request.POST
    form = CleaningForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = snkr_id
        new_cleaning.save()
    return redirect('snkr-detail', snkr_id=snkr_id)