from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice
from .forms import InvoiceForm

def invoice_list(request):
    """View to list all invoices."""
    invoices = Invoice.objects.all().order_by("-created_at")
    return render(request, "invoice/invoice_list.html", {"invoices": invoices})

def invoice_detail(request, pk):
    """View to show a single invoice."""
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, "invoice/invoice_detail.html", {"invoice": invoice})

def invoice_create(request):
    """View to create a new invoice."""
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoice_list")
    else:
        form = InvoiceForm()
    return render(request, "invoice/invoice_form.html", {"form": form})

def invoice_update(request, pk):
    """View to update an existing invoice."""
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect("invoice_list")
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, "invoice/invoice_form.html", {"form": form})

def invoice_delete(request, pk):
    """View to delete an invoice."""
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        invoice.delete()
        return redirect("invoice_list")
    return render(request, "invoice/invoice_confirm_delete.html", {"invoice": invoice})
