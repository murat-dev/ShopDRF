from django.urls import path
from .views import *

urlpatterns = [
    path('designer/', ProfileDesignerListView.as_view()),
    path('designer/<int:pk>/', ProfileDesignerDetailView.as_view()),
    path('designer-update/<int:pk>/', ProfileDesignerUpdateView.as_view()),
    path('customer/', ProfileCustomerListView.as_view()),
    path('customer/<int:pk>/', ProfileCustomerDetailView.as_view()),
    path('customer-update/<int:pk>/', ProfileCustomerUpdateView.as_view()),
]
