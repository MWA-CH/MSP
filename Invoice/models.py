from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid


class Customer(models.Model):
    """Model to store customer information."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """Model to store invoice information."""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('overdue', 'Overdue'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_number = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Temporarily nullable
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    due_date = models.DateField(default=now)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer.name}"

    @property
    def is_overdue(self):
        """Determine if the invoice is overdue."""
        return self.status == 'unpaid' and self.due_date < now().date()

    @property
    def calculate_total(self):
        """Calculate the total amount including tax."""
        return self.amount_due + (self.tax if self.tax else 0)
