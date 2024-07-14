from rest_framework import serializers
from .models import *
from superuser.models import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','first_name','last_name','email')

        def update(self, instance, validated_data):
            password = validated_data.get('password')
            
            instance.set_password(password)
        
            instance.save()
            return instance
        
class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','is_admin')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name')



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_image',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

