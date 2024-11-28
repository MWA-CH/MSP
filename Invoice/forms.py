from django import forms
from .models import Customer, Invoice


class CustomerForm(forms.ModelForm):
    """Form to manage Customer data."""

    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "postal_code",
            "country",
        ]


class InvoiceForm(forms.ModelForm):
    """Form to manage Invoice data."""

    class Meta:
        model = Invoice
        fields = [
            "customer",
            "invoice_number",
            "amount_due",
            "tax",
            "total",
            "status",
            "due_date",
            "notes",
        ]
