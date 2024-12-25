from rest_framework import serializers
from .models import Client, Company

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'company', 'is_active', 'phone_number']


class CompanySerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'website', 'created_at', 'clients']
