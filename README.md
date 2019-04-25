custom_jwt : custom_jwt is a simple Django app to provide authentication using jwt tokens.
============================================================================================


install with pip :

pip install -i https://test.pypi.org/simple/ custom-jwt



Quick start
-----------

1. Add "custom_jwt" to your INSTALLED_APPS setting like this::

   a)    INSTALLED_APPS = [
          ...
          ...
          'custom_jwt',
        ]
    
   b) Also add the JWT_AUTH in your settings file like this:
      set the values for expiry and refresh token as per your need.
        
        JWT_AUTH = {
            'JWT_AUTH_HEADER_PREFIX': 'bearer',
            'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
            'JWT_ALLOW_REFRESH': True,
            'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
            'JWT_RESPONSE_PAYLOAD_HANDLER': 'custom_jwt.views.jwt_response_payload_handler',
        }
        
   c) Make sure your settings file have have 'rest_framework.authentication.TokenAuthentication' in your 
      REST_FRAMEWORK > DEFAULT_AUTHENTICATION_CLASSES like this:
     
          REST_FRAMEWORK = {
                ...
                ...
                'DEFAULT_AUTHENTICATION_CLASSES': (
                    'rest_framework.authentication.SessionAuthentication',
                    'rest_framework.authentication.TokenAuthentication',
                    'rest_framework.authentication.BasicAuthentication',
                ),
                ...
            }
    
    
2. Include the auth URLconf in your project urls.py like this::

    path('auth/', include('custom_jwt.urls')),

3. Run `python manage.py migrate` to create the required models.

4. Start the development server and visit http://127.0.0.1:8000/auth/login or http://127.0.0.1:8000/auth/logout
   to use auth
   
