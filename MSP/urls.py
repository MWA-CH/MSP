from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),               # Admin site
    path("invoice/", include("Invoice.urls")),     # Invoice app URLs
    path("", lambda request: redirect("invoice/")),  # Redirect root URL to invoice list
]
