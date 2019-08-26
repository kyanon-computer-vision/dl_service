from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from apps.api.core.models import TimestampedModel

class Profile(TimestampedModel):
    SUBSCRIPTION = Choices('free', 'premium')

    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    # subscription = StatusField(choices_name=SUBSCRIPTION)
    subsciption = models.CharField(choices=SUBSCRIPTION, max_length=20)
    
