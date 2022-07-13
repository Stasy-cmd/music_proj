from rest_framework import permissions
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import CreateUserSerializer, LoginSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
