from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    client_name=serializers.CharField(source='client.name',read_only=True)
    owner_name=serializers.CharField(source='owner.username',read_only=True)
    
    class Meta:
        model = Project
        fields = ['id','name','description','client_name','owner_name']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


