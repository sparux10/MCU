from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from superuser.models import *
from rest_framework.permissions import IsAuthenticated

#get user info
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_role(request):
    user = request.user
    role = user.role
    role_serializer = RoleSerializer(role, many=True)
    return Response(role_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# Update user info
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete user
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

# Get profile image
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile_img(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)

# Update profile image
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_image(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(user_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Profile image updated successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete profile image
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile_img(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.profile_image:
        profile.profile_image.delete(save=False)
        profile.save()
        return Response({"message": "Profile image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "No profile image to delete"}, status=status.HTTP_400_BAD_REQUEST)

# Update address
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_address(request):
    user = request.user
    address = get_object_or_404(Address, user_id=user)
    serializer = AddressSerializer(address, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete address
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_address(request):
    address = get_object_or_404(Address, user_id=request.user.id)
    address.delete()
    return Response({'message': 'Address deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Get user addresses
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_addresses(request):
    addresses = Address.objects.filter(user_id=request.user)
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)
