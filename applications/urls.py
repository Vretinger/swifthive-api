from django.urls import path
from .views import ApplyForJobAPI

urlpatterns = [
    path('apply/', ApplyForJobAPI.as_view(), name='apply_for_job'),
]
