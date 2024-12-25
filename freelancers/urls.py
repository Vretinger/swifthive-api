from django.urls import path
from .views import FreelanceList, FreelancerDetail

urlpatterns = [
    path('freelancers/', FreelanceList.as_view(), name='freelance-list'),
    path('freelancers/<int:pk>/', FreelancerDetail.as_view(), name='freelance-detail'),
]
