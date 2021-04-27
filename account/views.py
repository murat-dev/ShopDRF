from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, CreateNewPasswordSerializer
from .tasks import send_activation_mail, send_activation_code

MyUser = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(MyUser, activation_code=activation_code)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Successfully activated', status=200)


# api/v1/accounts/forgot_password/?email=berdibaev.adyl@gmail.com
class ForgotPassword(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        user = get_object_or_404(MyUser, email=email)
        user.is_active = False
        user.create_activation_code()
        user.save()
        send_activation_code.delay(user.email, user.activation_code)
        return Response('Вам отправлено письмо', status=200)

class ForgotPasswordComplete(APIView):
    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Вы успешно восстановили пароль', status=200)
        



