from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route, CustomUserDetailsView
from dj_rest_auth.registration.views import RegisterView

urlpatterns = [
    # Root and admin
    path('', root_route, name='root'),
    path('admin/', admin.site.urls),

    # API-related routes
    path('api/auth/registration/', RegisterView.as_view(), name='custom-register'),
    path('api/auth/', include('dj_rest_auth.urls')),  # Includes login, password reset, etc.
    path('api/auth/logout/', logout_route, name='logout'),
    path('api/users/me/', CustomUserDetailsView.as_view(), name='user-details'),  # Current user's details

    # App-specific API routes
    path('api/job-listings/', include('job_listings.urls')),  
    path('api/accounts/', include('accounts.urls')),  
    path('api/applications/', include('applications.urls')),
    path('api/contact/', include('contact.urls')),
]
