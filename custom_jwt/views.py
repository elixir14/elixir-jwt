import logging
from django.contrib.auth import logout as django_logout
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from custom_jwt.permissions import IsTokenValid
from custom_jwt.serializers import UserSerializer
from custom_jwt.models import BlackListedToken

logger = logging.getLogger('app')


def jwt_response_payload_handler(token, user=None, request=None):
    user_data = (dict(UserSerializer(user, context={'request': request}).data))
    user_data['token'] = token
    return user_data


@api_view(["GET"])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsTokenValid,))
def logout(request):
    try:
        username = request.user.username
        logger.info("'%s' logout request.", username)
        logger.info("Adding user '%s' token in black listed token." % username)
        BlackListedToken.objects.create(
            token=str(request.auth),
            user=request.user
        )
        django_logout(request)
        logger.info("User '%s' logged out successfully." % username)
        return Response(
            {'msg': "'%s' logged out successfully." % username},
            status=status.HTTP_200_OK
        )
    except Exception as ex:
        logger.critical(
            "Caught exception in {}".format(__file__),
            exc_info=True
        )
        return Response(
            {"msg": ex.args},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
