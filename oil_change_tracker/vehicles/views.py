from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
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

class oilChangeCreateView(LoginRequiredMixin, CreateView):
    model = OilChangeRecord
    form_class = OilChangeForm
    template_name = 'oil_change_form.html'
    success_url = reverse_lazy('vehicle_list')

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=self.kwargs['vehicle_pk'])
        if self.vehicle.owner != request.user:
            return HttpResponseForbidden("Nedovolený přístup")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return super().form_valid(form)


class oilChangeUpdateView(LoginRequiredMixin, UpdateView):
    model = OilChangeRecord
    form_class = OilChangeForm
    template_name = 'oil_change_form.html'
    success_url = reverse_lazy('vehicle_list')

    def get_queryset(self):
        return OilChangeRecord.objects.filter(vehicle__owner=self.request.user)