from django.urls import path
from . import views

urlpatterns = [
    # User
    path('user/update/', views.update_user_info, name='update_user_info'),
    path('user/delete/', views.delete_user, name='delete_user'),
    path('user/', views.get_user_role, name='get_user'),
    path('user-info/', views.get_user, name='get_user'),

    # Profile
    path('profile-img/', views.get_profile_img, name='profile_img'),
    path('profile-img/update/', views.update_profile_image, name='profile_img_update'),
    path('profile-img/delete/', views.delete_profile_img, name='profile_img_delete'),

    # Addresses
    path('address/update/', views.update_address, name='update_address'),
    path('address/delete/', views.delete_address, name='delete_address'),
    path('address/', views.get_user_addresses, name='get_user_addresses'),
]
