from rest_framework.serializers import ModelSerializer
from .models import User, Message


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
