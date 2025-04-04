from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import vehicle
from .forms import VehicleForm

class vehicleListView(LoginRequiredMixin, ListView):
    model = vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

class vehicleDetailView(LoginRequiredMixin, DetailView):
    model = vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'

class vehicleCreateView(LoginRequiredMixin, CreateView):
    model = vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class vehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class vehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')