from django.urls import path
from . import views

urlpatterns = [
    path("", views.invoice_list, name="invoice_list"),  # Default view for invoice list
    path("create/", views.invoice_create, name="invoice_create"),  # Create new invoice
    path("<int:pk>/", views.invoice_detail, name="invoice_detail"),  # View invoice detail
    path("<int:pk>/update/", views.invoice_update, name="invoice_update"),  # Update invoice
    path("<int:pk>/delete/", views.invoice_delete, name="invoice_delete"),  # Delete invoice
]
