from rest_framework import permissions

SAFE_METHODS = ('GET')

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user and request.user.is_authenticated and request.user.is_admin:
                try:
                    user_permissions = request.user.role.name # Assuming `permissions` is a field in `role`
                    print(user_permissions,request.user)
                    if user_permissions == "full admin":
                        return True
                except AttributeError:
                    return False
        return False
            
class OnlyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_admin:
            try:
                user_permissions = request.user.role.permissions  # Assuming `permissions` is a field in `role`
                if user_permissions == "full admin":
                    return True
            except AttributeError:
                return False
        return False



