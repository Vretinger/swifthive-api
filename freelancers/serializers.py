from rest_framework import serializers
from .models import Freelancer


class FreelanceSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField() 

    class Meta:
        model = Freelancer
        fields = '__all__'

    def get_is_owner(self, obj):
        request = self.context.get('request') 
        if request and request.user == obj.user:
            return True
        return False
