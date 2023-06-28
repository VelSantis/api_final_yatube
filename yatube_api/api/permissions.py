from rest_framework import permissions


class IsAuthorPostOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.author
                or request.method
                in permissions.SAFE_METHODS)


class FollowReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":

            return (
                request.method or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return obj.author != request.user
