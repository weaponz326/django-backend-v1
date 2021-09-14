from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'location', 'about', 'photo']

class CustomRegisterSerializer(RegisterSerializer):
    location = serializers.CharField(required=True, max_length=255)
    about = serializers.CharField(required=True, )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['location'] = self.validated_data.get('location', '')
        data_dict['about'] = self.validated_data.get('about', '')
        return data_dict
