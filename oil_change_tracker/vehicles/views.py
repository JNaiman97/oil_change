from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle
from .forms import VehicleForm
from .models import OilChangeRecord
from .forms import OilChangeForm

class vehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)

class vehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)

class vehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class vehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)

class vehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)