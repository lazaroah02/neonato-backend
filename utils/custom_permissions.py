from django_graphene_permissions.permissions import BasePermission
from utils.exceptions import NotStaffException, NotAuthenticatedException

class IsStaff(BasePermission):
    """
    Allows access only to staff users.
    """

    @staticmethod
    def has_permission(context):
        if context.user.is_staff:
            return True
        raise NotStaffException 

class CustomIsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    @staticmethod
    def has_permission(context):
        if context.user and context.user.is_authenticated:
            return True
        raise NotAuthenticatedException     