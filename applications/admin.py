from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("listing", "applicant", "status", "applied_at")
    list_filter = ("status", "applied_at", "listing")
    search_fields = ("applicant__username", "listing__title")
    ordering = ("-applied_at",)
