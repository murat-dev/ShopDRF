from rest_framework import generics
from .models import ProfileDesigner, ProfileCustomer
from .serializers import ProfileDesignerSerializer, ProfileCustomerSerializer



class ProfileDesignerListView(generics.ListAPIView):
    queryset = ProfileDesigner.objects.all()
    serializer_class = ProfileDesignerSerializer

class ProfileDesignerDetailView(generics.RetrieveAPIView):
    queryset = ProfileDesigner.objects.all()
    serializer_class = ProfileDesignerSerializer

class ProfileDesignerUpdateView(generics.UpdateAPIView):
    queryset = ProfileDesigner.objects.all()
    serializer_class = ProfileDesignerSerializer



class ProfileCustomerListView(generics.ListAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer

class ProfileCustomerDetailView(generics.RetrieveAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer

class ProfileCustomerUpdateView(generics.UpdateAPIView):
    queryset = ProfileCustomer.objects.all()
    serializer_class = ProfileCustomerSerializer




