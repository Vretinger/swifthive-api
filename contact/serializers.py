from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True, max_length=255)
    message = serializers.CharField(required=True)
    freelancer_email = serializers.EmailField(required=True)
