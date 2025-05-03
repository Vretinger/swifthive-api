# serializers.py
from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    applicant_count = serializers.SerializerMethodField()
    company = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['created_by']

    def get_applicant_count(self, obj):
        return obj.applications.count()

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
