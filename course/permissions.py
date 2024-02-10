from rest_framework.permissions import BasePermission, IsAuthenticated



class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().author


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.group == 'moder'

class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return IsAuthenticated().has_permission(request, view)
        elif request.method in ['GET', 'PATCH']:
            return IsAuthenticated().has_permission(request, view) and (IsAuthor().has_permission(request, view) or IsModer().has_permission(request, view))
        elif request.method == 'DELETE':
            return IsAuthor().has_permission(request, view)
        return False