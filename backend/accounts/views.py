from typing import TYPE_CHECKING
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

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