from rest_framework import serializers as sz
from apps.api.authentication.models import User
from apps.api.core.serializers import UserSerializer
from .models import VisionDataset, VisionDLModel


class VisionDatasetSerializerForCreate(sz.ModelSerializer):
    user    = UserSerializer(read_only=True)
    labels  = sz.ListField(allow_empty=True, child=sz.CharField(max_length=50))

    class Meta:
        model = VisionDataset
        fields = '__all__'

class VisionDatasetSerializerForList(sz.ModelSerializer):
    status  = sz.CharField(source='get_status_display')
    dataset_type = sz.CharField(source='get_dataset_type_display')

    class Meta:
        model = VisionDataset
        fields = ('id', 'name', 'last_modified', 'total_samples', 'total_classes', 'status', 'dataset_type')

class VisionDatasetDetailSerializer(sz.ModelSerializer):
    user = UserSerializer(read_only=True) 
    labels = sz.ListField(allow_empty=True, child=sz.CharField(max_length=30))
    status  = sz.CharField(source='get_status_display')
    dataset_type = sz.CharField(source='get_dataset_type_display')

    class Meta:
        model = VisionDataset
        fields = '__all__'

# DL Model serializers

class VisionDLModelSerializerForList(sz.ModelSerializer):
    model_type = sz.CharField(source='get_model_type_display')
    
    class Meta:
        model = VisionDLModel
        fields = ('id', 'name', 'last_modified', 'model_type')

class VisionDLModelSerializerForCreate(sz.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = VisionDLModel
        fields = '__all__'

class VisionDLModelDetailSerializer(sz.ModelSerializer):
    user = UserSerializer(read_only=True)
    model_type = sz.CharField(source='get_model_type_display')

    class Meta:
        model = VisionDLModel
        fields = '__all__'
