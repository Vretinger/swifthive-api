from django.urls import path
from .views import ClientList, ClientDetail

urlpatterns = [
    path('api/clients/', ClientList.as_view(), name='client_list'),
    path('api/clients/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
]
