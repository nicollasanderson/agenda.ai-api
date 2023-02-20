import jwt

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from users.models import User
from users.permissions import IsSuperUserPermission, IsUserOwnerPermission
from users.serializers import (
    LoginSerializer,
    UpdateUserSerializer,
    UserSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import os, dotenv, datetime

# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["id"] = str(user.id)
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["is_professor"] = user.is_professor
        token["is_admin"] = user.is_superuser

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         verify = serializer.is_valid()

#         if not verify:
#             return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

#         if not request.data:
#             return Response(
#                 {"Error": "Por favor, utiize um email/password"}, status="400"
#             )

#         email = serializer.validated_data["email"]
#         password = serializer.validated_data["password"]
#         # try:
#         user = authenticate(
#             email=email,
#             password=password,
#         )

#         if user:
#             payload = {
#                 "id": str(user.id),
#                 "email": user.email,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "is_professor": user.is_professor,
#                 "iat": datetime.datetime.now(),
#             }
#             jwt_token = {"token": jwt.encode(payload, os.getenv("SECRET_KEY"))}

#             return Response(jwt_token, status=200, content_type="application/json")
#         else:
#             return Response(
#                 {"Error": "Credenciais inválidas"},
#                 status=400,
#                 content_type="application/json",
#             )


class CreateUserView(generics.CreateAPIView):
    permission_classes = [IsSuperUserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUsersView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwnerPermission]

    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
