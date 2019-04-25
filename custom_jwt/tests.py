
from rest_framework.test import APITestCase


class TestBlackListedTokens(APITestCase):
    fixtures = ['custom_jwt.json']

    def login(self):
        pass
