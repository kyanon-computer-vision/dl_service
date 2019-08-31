from rest_framework.exceptions import APIException
from apps.api.core.constants import MSG_PROF_NOT_EXISTS

class ProfileDoesNotExits(APIException):
    status_code = 400
    default_detail = MSG_PROF_NOT_EXISTS