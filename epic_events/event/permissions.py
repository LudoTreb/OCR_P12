from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        user = request.user
        if user.is_superuser:
            return True
        elif request.method == 'DELETE':
            return False
        elif user.groups.filter(name='sales').exists():
            return True
        elif user.groups.filter(name='management').exists():
            return request.method in permissions.SAFE_METHODS
        elif user.groups.filter(name='support').exists():
            return request.method in ['GET', 'PUT', 'PATCH']
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # import pdb;
        # pdb.set_trace()
        user = request.user
        if user.is_superuser:
            return True

        elif user.groups.filter(name="sales").exists():
            return request.method in ['GET', 'PUT']
        elif user.groups.filter(name='management').exists():
            return request.method in permissions.SAFE_METHODS
        elif user.groups.filter(name='support').exists():
            if user == obj.support_contact and obj.event_status is True:
                return request.method in ['GET', 'PUT', 'PATCH']
        else:
            return False
