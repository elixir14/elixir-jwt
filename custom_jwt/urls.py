from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken

from custom_jwt.views import logout

urlpatterns = [
    path('login/', ObtainJSONWebToken.as_view(), name='login'),
    path('logout/', logout, name='logout'),

]
