from django.urls import path, include
from .views import CustomRegisterView, FreelancerListView, FreelancerDetailView, ClientListView, ClientDetailView
from dj_rest_auth import views as dj_rest_auth_views

urlpatterns = [
    # Custom registration view
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom-register'),
    
    # Default dj-rest-auth URLs (including login, logout, password reset, etc.)
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    path('freelancers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('freelancers/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
