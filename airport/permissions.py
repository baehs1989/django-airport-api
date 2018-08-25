from rest_framework import permissions

class AirportApiPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser



class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser or request.method in permissions.SAFE_METHODS

