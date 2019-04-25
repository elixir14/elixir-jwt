from rest_framework.permissions import BasePermission
from custom_jwt.models import BlackListedToken


class IsTokenValid(BasePermission):
    message = 'Signature has expired.'

    def has_permission(self, request, view):
        user_id = request.user.id
        token = request.auth
        return not BlackListedToken.objects.filter(user=user_id, token=token).exists()
