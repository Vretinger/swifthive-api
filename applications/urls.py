from django.urls import path
from .views import (
    ApplyForJobAPI,
    ListUserApplicationsAPI,
    ListJobApplicationsAPI,
    UpdateApplicationStatusAPI,
    HasAppliedAPI
)

urlpatterns = [
    path("apply/", ApplyForJobAPI.as_view(), name="apply-for-job"),
    path("my/", ListUserApplicationsAPI.as_view(), name="my-applications"),
    path("list/<int:listing_id>/", ListJobApplicationsAPI.as_view(), name="job-applications"),
    path("update/<int:pk>/", UpdateApplicationStatusAPI.as_view(), name="update-application"),
    path("has-applied/<int:listing_id>/", HasAppliedAPI.as_view(), name="has-applied"),
]