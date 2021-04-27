from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Category, Product, Review, Like, Favorite
from .serializers import CategoryListSerializer, ProductSerializer, ReviewSerializer, CategoryDetailSerializer, \
    NewsSerializer, FavoriteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .permissions import IsAuthorProductPermission, IsDesignerPermission, IsCustomerPermission, IsAuthorReviewPermission
from .utils import main
from django_filters.rest_framework import DjangoFilterBackend


class PaginationProduct(PageNumberPagination):
    page_size = 5

class PaginationReview(PageNumberPagination):
    page_size = 10


class PermissionMixinProduct:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsDesignerPermission, ]
        elif self.action in ['update', 'partial_update', 'delete']:
            permissions = [IsAuthorProductPermission, ]
        else:
            permissions = [AllowAny, ]
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

class PermissionMixinReview:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsCustomerPermission, ]
        elif self.action in ['update', 'partial_update', 'delete']:
            permissions = [IsAuthorReviewPermission, ]
        else:
            permissions = [AllowAny, ]
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny, ]

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductViewSet(PermissionMixinProduct, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationProduct
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', ]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        product = self.get_object()
        obj, created = Like.objects.get_or_create(user=request.user.profile_customer, product=product)
        if not created:
            obj.like = not obj.like
            obj.save()
        liked_or_unliked = 'liked' if obj.like else 'unliked'
        return Response('Successfully {} product'.format(liked_or_unliked), status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        product = self.get_object()
        obj, created = Favorite.objects.get_or_create(user=request.user.profile_customer, product=product)
        if not created:
            obj.favorite = not obj.favorite
            obj.save()
        added_removed = 'added' if obj.favorite else 'removed'
        return Response('Successfully {} favorite'.format(added_removed), status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewViewSet(PermissionMixinReview, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PaginationReview

class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        qs = self.request.user.profile_customer
        queryset = Favorite.objects.filter(user=qs, favorite=True)
        return queryset


class News(APIView):
    def get(self, request):
        info = main()
        serializer = NewsSerializer(instance=info, many=True)
        return Response(serializer.data)



