from rest_framework import permissions


class EventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True

        if request.method == "DELETE":
            return False

        if user.groups.filter(name__in=["support", "management"]):
            return True
        if user.groups.filter(
            name__in=[
                "sales",
            ]
        ):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        if user.groups.filter(name__in=["support", "management"]):
            return True
        if user.groups.filter(name__in=["sales", "management"]):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
