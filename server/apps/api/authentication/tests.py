import json

from apps.api.authentication.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("users:list")
    
