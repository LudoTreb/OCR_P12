from rest_framework import permissions


class EmployeePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name__in=['sales', 'support', 'management']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
