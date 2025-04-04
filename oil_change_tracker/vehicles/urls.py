from django.urls import path
from.views import vehicleListView, vehicleDetailView, vehicleCreateView, vehicleUpdateView, vehicleDeleteView

urlpatterns = [
    path('list/', vehicleListView.as_view(), name="vehicle_list"),
    path('vehicles/<int:pk>/', vehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/add/', vehicleCreateView.as_view(), name='vehicle-add'),
    path('vehicles/<int:pk>/edit/', vehicleUpdateView.as_view(), name='vehicle-edit'),
    path('vehicles/<int:pk>/delete/', vehicleDeleteView.as_view(), name='vehicle-delete'),
]