from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom-register'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
