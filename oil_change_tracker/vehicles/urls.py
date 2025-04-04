from django.urls import path

path('vehicles/<int:pk>/', vehicleDetailView.as_view(), name='vehicle-detail'),
path('vehicles/add/', vehicleCreateView.as_view(), name='vehicle-add'),
path('vehicles/<int:pk>/edit/', vehicleUpdateView.as_view(), name='vehicle-edit'),
path('vehicles/<int:pk>/delete/', vehicleDeleteView.as_view(), name='vehicle-delete'),