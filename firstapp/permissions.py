from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self,request,view,obj):

        if request.method in SAFE_METHODS:
            return True

        else:
            return obj.owner==request.user

class IsStaffOnlyDelete(BasePermission):
     def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
           return True

        if request.method is "DELETE":
           return request.user.is_staff
    
        return obj.owner==request.user
    