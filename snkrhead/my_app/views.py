from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Shoe
from .forms import CleaningForm


@login_required
def snkr_index(request):
    shoes = Shoe.objects.filter(user=request.user) 
    return render(request, 'shoes/index.html', {'shoes': shoes})


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def snkr_detail(request, snkr_id):
    shoe = Shoe.objects.get(id=snkr_id)
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', {'shoe': shoe, 'cleaning_form': cleaning_form})

class SnkrCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class SnkrUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['amount', 'description', 'image']

class SnkrDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/snkrs/'

@login_required
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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('snkr-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)