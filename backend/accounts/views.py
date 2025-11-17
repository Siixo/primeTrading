from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from typing import TYPE_CHECKING
from rest_framework_simplejwt.authentication import JWTAuthentication

#Importing TokenObtainPairView and TokenObtainPairSerializer in order to fix last_login error in database since it's not automatically updated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone

from .serializers import (
    UserRegistrationSerializer, 
    UserSerializer, 
    ChangePasswordSerializer
)

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    User registration view.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **karwgs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Get or update the current user's profile
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self):  # type: ignore[override]
        # Return the current authenticated user
        return self.request.user
    
class ChangePasswordView(APIView):
    """
    Change password view for authenticated users.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, 
            context={'request': request}
        )
        if serializer.is_valid():
            # Type checker: after is_valid(), validated_data is guaranteed to be a dict
            new_password: str = serializer.validated_data['new_password']  # type: ignore[index]
            request.user.set_password(new_password)
            request.user.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogoutView(APIView):
    """
    Logout view to blacklist the refresh token.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            Refresh_token = request.data.get('refresh_token')
            if not Refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(Refresh_token)
            token.blacklist()
            return Response({"message": "User logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT token pair and set HttpOnly cookies.
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.get_user(request)
        
        if user:
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
        
        # Get tokens from serializer
        access = serializer.validated_data.get('access')
        refresh = serializer.validated_data.get('refresh')
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        
        # Set HttpOnly cookies so we don't have to handle tokens in frontend
        if access:
            response.set_cookie(
                'access_token', access,
                httponly=True, secure=True, samesite='Lax'
            )
        if refresh:
            response.set_cookie(
                'refresh_token', refresh,
                httponly=True, secure=True, samesite='Lax'
            )
        return response

    def get_user(self, request):
        username = request.data.get('username')
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
