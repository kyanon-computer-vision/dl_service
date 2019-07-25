import re
from email.utils import parseaddr

from .constants import (
    MSG_EMAIL_INVALID,
    MSG_EMAIL_NOT_EMPTY,
    MSG_USER_NOT_EMPTY,
    MSG_USERNAME_SHORT,
    STC_MIN_LEN_USERNAME
)

def validate_username(username):
    if username is None or len(username) == 0:
        return False, MSG_USER_NOT_EMPTY
    if len(username) < STC_MIN_LEN_USERNAME:
        return False, MSG_USERNAME_SHORT
    return True, None

def validate_email(email):
    if email is None or len(email) == 0:
        return False, MSG_EMAIL_NOT_EMPTY
    if parseaddr(email)[1] == '':
        #email is invalid
        return False, MSG_EMAIL_INVALID
    return True, None