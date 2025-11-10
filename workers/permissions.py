from rest_framework import permissions

class IsAdminOrObserver(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser or request.user.groups.filter(name='Admin').exists():
                return True
            if request.user.groups.filter(name='Observer').exists():
                if view.action in ['update', 'partial_update']:
                    return True
        return False

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            return request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
        return False

class WorkerPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated:
            is_admin = request.user.is_superuser or request.user.groups.filter(name='Admin').exists()
            is_observer = request.user.groups.filter(name='Observer').exists()

            if is_admin:
                return True

            if is_observer and view.action in ['update', 'partial_update', 'move_worker']:
               return True

        return False
