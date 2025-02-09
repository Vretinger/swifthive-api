from django.urls import path
from .views import CreateListingAPI, ListListingsAPI, EditDeleteListingAPI

urlpatterns = [
    path("listings/", ListListingsAPI.as_view(), name="list_listings"),
    path("listings/create/", CreateListingAPI.as_view(), name="create_listing"),
    path("listings/<int:pk>/", EditDeleteListingAPI.as_view(), name="edit_delete_listing"),
]
