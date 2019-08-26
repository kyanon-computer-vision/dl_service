from django.db import models
from model_utils import Choices
from apps.api.core.models import BaseDataset, BaseDLModel
from apps.api.core.constants import DEFAULT_VISION_MODEL_TYPE, CHOICES_VISION_MODE_TYPE

class VisionDataset(BaseDataset):
    domain          = models.CharField(default='General', max_length=30)
    dataset_type    = models.SmallIntegerField(choices=CHOICES_VISION_MODE_TYPE, default=DEFAULT_VISION_MODEL_TYPE)

# class VisionDLModel(BaseDLModel):
#     class Meta:
#         abstract = True

