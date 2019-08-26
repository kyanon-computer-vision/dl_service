from rest_framework import serializers as sz
from apps.api.authentication.models import User
from apps.api.core.models import StringObject
from .models import VisionDataset

class DatasetUserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class VisionDatasetSerializer(sz.ModelSerializer):
    labels  = sz.ListField(allow_empty=True, child=sz.CharField(max_length=50))
    user    = DatasetUserSerializer(read_only=True)

    class Meta:
        model = VisionDataset
        # fields = ('name', 'total_samples', 'total_classes', 'status', 'dataset_type')
        fields = '__all__'

class VisionDatasetDetailSerializer(sz.ModelSerializer):
    labels = sz.ListField(allow_empty=True, child=sz.CharField(max_length=30))
    user = DatasetUserSerializer(read_only=True)

    class Meta:
        model = VisionDataset
        fields = '__all__'
