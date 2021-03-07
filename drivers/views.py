from django.shortcuts import render, redirect
from django.views import  generic
from .models import Driver
from .forms import DriverForm
from django.http import HttpResponse
from django.urls import reverse

class DriversIndexView(generic.ListView):
    template_name = 'drivers/index.html'
    context_object_name = 'drivers'

    def get_queryset(self):
        return Driver.objects.all()


class DriversDetailView(generic.DetailView):
    template_name = 'drivers/detail.html'
    model = Driver


def create(request):
    if request.method == 'GET':
        form = DriverForm()
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            Driver.objects.create(name=form.cleaned_data['name'], license=form.cleaned_data['license'])
            return redirect(reverse('drivers:index'))
            
    return render(request, 'drivers/create.html', {'form': form})