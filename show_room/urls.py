from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from main.views import ProductViewSet, ReviewViewSet
from cart.views import CartViewSet


schema_view = get_schema_view(
    openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=[AllowAny, ],
)

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('review', ReviewViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui()),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/profile/', include('myprofile.urls')),
    path('api/v1/', include('main.urls')),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)