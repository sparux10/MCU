# authapp/serializers.py
from rest_framework import serializers
from superuser.models import MyUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name','email', 'password']

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

