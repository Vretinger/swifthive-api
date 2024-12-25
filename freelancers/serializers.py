from rest_framework import serializers
from .models import Freelancer


class FreelanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Freelancer
        fields = '__all__'