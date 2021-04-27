from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account.views import (RegistrationView, ActivationView, ForgotPassword, ForgotPasswordComplete)

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('forgot_password/', ForgotPassword.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplete.as_view()),
]
