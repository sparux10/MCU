from rest_framework import serializers
from .models import MyUser, Role
from django.contrib.auth.hashers import make_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','name']  # تأكد من أن هذه الحقول موجودة في نموذج Role
        
class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_admin', 'last_login', 'role', 'role_id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['password'] = make_password(password)
        role_id = validated_data.pop('role_id', None)
        user = MyUser.objects.create(**validated_data)
        if role_id:
            user.role_id = role_id.id
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        validated_data['password'] = make_password(password)
        role_id = validated_data.pop('role_id', None)
        instance = super().update(instance, validated_data)
        if role_id:
            instance.role_id = role_id.id
        instance.save()
        return instance
    def get_role(self, instance):
        if instance.role:
            return instance.role.name
        return None
    
    def get_role_id(self, instance):
        if instance.role:
            return instance.role.name
        return None