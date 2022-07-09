from rest_framework import permissions

class ListCrateSchedulePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated)

class IsUserOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser