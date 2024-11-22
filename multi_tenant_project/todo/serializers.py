from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TodoSerializer(serializers.ModelSerializer):
    client_name=serializers.CharField(source='client.name',read_only=True)
    owner_name=serializers.CharField(source='owner.username',read_only=True)

    class Meta:
        model = Todo
        fields = ['client_name','owner_name','title','description','completed','created_at','completion_time']
