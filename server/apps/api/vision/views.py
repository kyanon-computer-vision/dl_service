# pylint: no-member
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .renderers import VisionDatasetJSONRenderer
from .serializers import VisionDatasetSerializer, VisionDatasetDetailSerializer
from .models import VisionDataset
from .permissions import UserIsOwnerDataset

class _VisionDatasetAPIView(ModelViewSet):
    permission_classes  = (IsAuthenticated,)
    renderer_classes    = (VisionDatasetJSONRenderer,)
    
    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        if self.action == 'list':
            return VisionDatasetSerializer
        elif self.action == 'retrieve':
            return VisionDatasetDetailSerializer
        

class VisionDatasetAPIView(ListCreateAPIView):
    permission_classes  = (IsAuthenticated,)
    renderer_classes    = (VisionDatasetJSONRenderer,)
    serializer_class    = VisionDatasetSerializer

    def get_queryset(self):
        return VisionDataset.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        _data = request.data.get('dataset', {})
        serializer = self.serializer_class(data=_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisionDatasetDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class    = VisionDatasetSerializer
    queryset            = VisionDataset.objects.all()
    permission_classes  = (IsAuthenticated, UserIsOwnerDataset,)
    renderer_classes    = (VisionDatasetJSONRenderer,)

