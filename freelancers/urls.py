from django.urls import path
from freelancers import views

urlpatterns = [
    path('freelancers/', views.FreelanceList.as_view()),
]