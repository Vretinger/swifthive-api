# clients/admin.py
from django.contrib import admin
from .models import Company, Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']  # Include is_active and created_at

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']  # Include is_active and created_at

admin.site.register(Client, ClientAdmin)
admin.site.register(Company, CompanyAdmin)
