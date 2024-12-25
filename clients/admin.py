# clients/admin.py
from django.contrib import admin
from .models import Company, Client, Listing

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Listing)
