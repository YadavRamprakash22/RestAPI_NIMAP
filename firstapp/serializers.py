from rest_framework import serializers
from .models import User, Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']




class ClientSerializer(serializers.ModelSerializer):
    # created_by=UserSerializer(read_only=True)
    # projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=Client
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)
    # users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'created_at','users', 'created_by']
