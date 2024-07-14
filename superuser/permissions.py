from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_admin:
                if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
                    return True
                else:
                    user_permissions = request.user.role
                    print(user_permissions)  
                    if str(user_permissions) == "full admin":
                        return True
                    else:
                        return False
            else:
                return False  # Deny access for users with other roles
        else:
            return False  # Deny access for unauthenticated users