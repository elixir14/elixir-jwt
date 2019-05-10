
import datetime

REST_FRAMEWORK = {'EXCEPTION_HANDLER': 'custom_jwt.exceptions.custom_exception_handler'}

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'bearer',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1000),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'custom_jwt.views.jwt_response_payload_handler',
}