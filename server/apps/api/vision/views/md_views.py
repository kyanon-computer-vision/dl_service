# pylint: disable=no-member

from rest_framework import (
    status,
    response,
    permissions,
    exceptions,
    generics
)

from apps.api.core.utils import MethodSerializerView
from ..renderers import VisionDLModelJSONRenderer
from ..serializers import (
    VisionDLModelDetailSerializer,
    VisionDLModelSerializerForCreate,
    VisionDLModelSerializerForList
)
from ..models import VisionDLModel
from ..permissions import UserIsOwnerModel

class VisionDLModelAPIView(MethodSerializerView, generics.ListCreateAPIView):
    permission_classes  = (permissions.IsAuthenticated,)
    renderer_classes    = (VisionDLModelJSONRenderer)

    method_serializer_classes = {
        ('GET',): VisionDLModelSerializerForList,
        ('POST',): VisionDLModelSerializerForCreate
    }
    
    def get_queryset(self):
        return VisionDLModel.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        _data = request.data.get('model', {})
        ser_class = self.get_serializer_class()
        serializer = ser_class(data=_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisionDLModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class    = VisionDLModelDetailSerializer
    queryset            = VisionDLModel.objects.all()
    permission_classes  = (permissions.IsAuthenticated, UserIsOwnerModel)
    renderer_classes    = (VisionDLModelJSONRenderer)
