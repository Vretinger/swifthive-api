from django.urls import path
from .views import FreelanceList, FreelancerDetail

urlpatterns = [
    path('', FreelanceList.as_view(), name='freelance-list'),
    path('<int:pk>/', FreelancerDetail.as_view(), name='freelance-detail'),
]
