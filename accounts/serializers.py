from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User

class CustomUserSlz(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'is_student', 'is_teacher')

class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'is_student', 'is_teacher')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user

class TokenSerializer(serializers.ModelSerializer):
        user_type = serializers.SerializerMethodField()

        class Meta:
            model = Token
            fields = ('key', 'user', 'user_type')

        def get_user_type(self, obj):
            serializer_data = CustomUserSlz(
                obj.user
            ).data
            is_student = serializer_data.get('is_student')
            is_teacher = serializer_data.get('is_teacher')
            return {
                'is_student': is_student,
                'is_teacher': is_teacher
            }
