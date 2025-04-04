from django.urls import path
from.views import vehicleListView, vehicleDetailView, vehicleCreateView, vehicleUpdateView, vehicleDeleteView

urlpatterns = [
    path('list/', vehicleListView.as_view(), name="vehicle_list"),
    path('vehicles/<int:pk>/', vehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicles/add/', vehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicles/<int:pk>/edit/', vehicleUpdateView.as_view(), name='vehicle_form'),
    path('vehicles/<int:pk>/delete/', vehicleDeleteView.as_view(), name='vehicle_confirm_delete'),

    path('vehicles/<int:vehicle_pk>/oilchange/add/', oilChangeCreateView.as_view(), name='oilchange_add'),
    path('oilchange/<int:pk>/edit/', oilChangeUpdateView.as_view(), name='oilchange_edit')
]