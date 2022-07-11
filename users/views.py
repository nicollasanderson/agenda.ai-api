import email
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from users.models import User
from users.permissions import IsSuperUserPermission, IsUserOwnerPermission
from users.serializers import LoginSerializer, UpdateUserSerializer, UserReturnSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        verify = serializer.is_valid()

        if not verify:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if user:
            
            user_data = {
                'email':user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_professor': user.is_professor
            }

            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key, 'user': user_data})

        return Response({"detail":"invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUsersView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwnerPermission]

    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer