from django.contrib import admin
from .models import Customer, Invoice  # Use a relative import for models

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'amount_due', 'status', 'due_date')
    search_fields = ('invoice_number', 'customer__name')
    list_filter = ('status', 'due_date')
