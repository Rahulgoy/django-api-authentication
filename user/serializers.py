
"""
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',
                  'email', 'name', 'phone')

    def validate(self, attrs):
        if len(str(attrs['phone'])) != 10:
            raise serializers.ValidationError(
                {"phone": "Phone number should not be less than or greater than 10 characters."})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError(
                {"password": "Password should not be less than 8 characters."})

        return attrs
 """
""" def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            phone=validated_data['phone']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user """


""" 
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(write_only=True)
    phone = serializers.IntegerField()
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
 """
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'name', 'password', 'phone')

        def validate(self, attrs):
            if len(str(attrs['phone'])) != 10:
                raise serializers.ValidationError(
                    {"phone": "Phone number should not be less than or greater than 10 characters."})
            if len(attrs['password']) < 8:
                raise serializers.ValidationError(
                    {"password": "Password should not be less than 8 characters."})

            return attrs
