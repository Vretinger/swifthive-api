from django.urls import path
from .views import FreelancerListView, FreelancerDetailView, ClientListView, ClientDetailView, SkillListView


urlpatterns = [
    path('freelancers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('freelancers/<int:custom_user_id>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:custom_user_id>/', ClientDetailView.as_view(), name='client-detail'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
]
