from django.urls import path, include
from .views import CustomRegisterView
from dj_rest_auth import views as dj_rest_auth_views

urlpatterns = [
    # Custom registration view
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom-register'),
    
    # Default dj-rest-auth URLs (including login, logout, password reset, etc.)
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
