from django.shortcuts import render, redirect
from django.views import generic
from .models import Car
from .forms import CarForm
from django.urls import reverse


class CarsIndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all()


class CarsDetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'


def create(request):
    if request.method == 'GET':
        form = CarForm()
    else:
        form = CarForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            vin = form.cleaned_data['vin']
            owner = form.cleaned_data['owner']
            
            Car.objects.create(brand=brand, model=model, year=year, vin=vin, owner=owner)
            return redirect(reverse('cars:index'))

    
    return render(request, 'cars/create.html', {'form': form})