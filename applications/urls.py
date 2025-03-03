from django.urls import path
from .views import ApplyJobView, MyApplicationsView, JobApplicationsView, UpdateApplicationStatusView

urlpatterns = [
    path("applications/apply/", ApplyJobView.as_view(), name="apply-job"),  # Freelancer applies
    path("applications/my/", MyApplicationsView.as_view(), name="my-applications"),  # Freelancer views their apps
    path("applications/<int:listing_id>/", JobApplicationsView.as_view(), name="job-applications"),  # Client views applicants
    path("applications/<int:id>/", UpdateApplicationStatusView.as_view(), name="update-application"),  # Client updates status
]
