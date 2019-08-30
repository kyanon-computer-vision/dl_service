# pylint: disable=no-member

from rest_framework import (
    status,
    response,
    permissions,
    exceptions,
    generics
)

from apps.api.core.utils import MethodSerializerView
from ..renderers import VisionDatasetJSONRenderer
from ..serializers import (
    VisionDatasetDetailSerializer,
    VisionDatasetSerializerForCreate,
    VisionDatasetSerializerForList
)
from ..models import VisionDataset
from ..permissions import UserIsOwnerDataset

class VisionDatasetAPIView(MethodSerializerView, generics.ListCreateAPIView):
    permission_classes  = (permissions.IsAuthenticated,)
    renderer_classes    = (VisionDatasetJSONRenderer,)

    method_serializer_classes = {
        ('GET',): VisionDatasetSerializerForList,
        ('POST', ): VisionDatasetSerializerForCreate
    }
    
    def get_queryset(self):
        return VisionDataset.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        _data = request.data.get('dataset', {})
        ser_class = self.get_serializer_class()
        serializer = ser_class(data=_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)        

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisionDatasetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class    = VisionDatasetDetailSerializer
    queryset            = VisionDataset.objects.all()
    permission_classes  = (permissions.IsAuthenticated, UserIsOwnerDataset,)
    renderer_classes    = (VisionDatasetJSONRenderer,)