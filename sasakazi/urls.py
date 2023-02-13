from django.urls import path
from .views import (
    CustomerListCreateAPIView,
    AccountListCreateAPIView,
    CardListCreateAPIView,
    home
)
urlpatterns=[
    path('', home),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customer/<int:id>', CustomerListCreateAPIView.as_view(), name='cutomer-id'),
    path('accounts/', AccountListCreateAPIView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountListCreateAPIView.as_view(), name='account-retrieve-update-destroy'),
    path('cards/', CardListCreateAPIView.as_view(), name='card-list-create'),
    path('cards/<int:pk>/', CardListCreateAPIView.as_view(), name='card-retrieve-update-destroy'),
    
]

