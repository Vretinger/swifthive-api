from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "Company", "category", "location", "is_active", "created_at")
    list_filter = ("category", "is_active", "created_at", "Company")
    search_fields = ("title", "Company__name", "location")
    ordering = ("-created_at",)  # Show newest listings first
