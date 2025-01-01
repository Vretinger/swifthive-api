from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route, CustomUserDetailsView
from dj_rest_auth.registration.views import RegisterView
from accounts.serializers import CustomRegisterSerializer

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # default routes
    path('dj-rest-auth/registration/', RegisterView.as_view(serializer_class=CustomRegisterSerializer)),
    path('dj-rest-auth/logout/', logout_route),

    # Custom user details view, this overrides the default one
    path('user/', CustomUserDetailsView.as_view(), name='user-details'),

    path('', include('freelancers.urls')),
    path('clients/', include('clients.urls')), 
    path('job-listings/', include('job_listings.urls')), 
    path('accounts/', include('accounts.urls')),
]

