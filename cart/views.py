from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from .permissions import IsAuthorPermission, IsCustomerPermission


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsCustomerPermission, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class CartViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        qs = self.request.user.profile_customer
        queryset = super().get_queryset()
        queryset = queryset.filter(user=qs)
        return queryset



