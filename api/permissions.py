from rest_framework import permissions

class IsTeacherorStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_teacher or request.user.is_staff



class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwnerorStaff(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
    
        return obj == request.user or  request.user.is_staff or request.user.is_teacher