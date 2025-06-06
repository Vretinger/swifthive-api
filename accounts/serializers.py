from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser, FreelancerProfile, ClientProfile, Skill, Category, Company

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Disable the 'username' field
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    company = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def validate(self, data):
        role = data.get('role')
        if role == 'client' and not data.get('company'):
            raise serializers.ValidationError({'company': "This field is required for clients."})
        elif role not in dict(CustomUser.ROLE_CHOICES).keys():
            raise serializers.ValidationError({'role': "Invalid role specified."})
        return data

    def save(self, request):
        # Get or create Company instance if user is a client
        company_instance = None
        if self.validated_data['role'] == 'client' and self.validated_data.get('company'):
            company_name = self.validated_data['company']
            company_instance, _ = Company.objects.get_or_create(name=company_name)

        user = CustomUser.objects.create(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            role=self.validated_data['role'],
            company=company_instance
        )

        user.set_password(self.validated_data['password1'])
        user.save()
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk')
    company = serializers.StringRelatedField()

    class Meta:
        model = CustomUser
        fields = ['id','email', 'first_name', 'last_name', 'role', 'company', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    
class FreelancerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = FreelancerProfile
        fields = [
            'id',
            'user',
            'user_id',
            'bio',
            'custom_skills',
            'experience',
            'portfolio_link',
            'hourly_rate',
            'location',
            'availability_status',
            'profile_picture',
            'created_at',
            'updated_at',
            'skills',
        ]

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return None

class ClientProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ClientProfile
        fields = '__all__'

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer for the Skill model
class SkillSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested category data

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category']