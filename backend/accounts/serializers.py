from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
import re

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    #Email field with unique validation
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    #Password fields with validation
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        #Check if passwords match 
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        
        #Check if username is not empty and correct lenghth
        username  =attrs.get('username', '')
        if not username or len(username) < 3:
            raise serializers.ValidationError({"username": "Username must be at least 3 characters long."})
        if len(username) > 150:
            raise serializers.ValidationError({"username": "Username must be less than 150 characters long."})
        
        #Check if username contains only alphanumeric characters
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            raise serializers.ValidationError({"username": "Username contains invalid characters. Only alphanumeric characters and underscores are allowed."})

        return attrs
    
    #Create user method to save user to database
    def create(self, validated_data):
        validated_data['email'] = validated_data['email'].lower().strip()
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, validators=[validate_password], write_only=True)

    def validate(self, attrs):
        # Prevent reusing the same password
        if attrs.get('old_password') == attrs.get('new_password'):
            raise serializers.ValidationError({"new_password": "New password must be different from the old password."})
        return attrs

    def validate_old_password(self, value):
        # Check if the old password is correct
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value