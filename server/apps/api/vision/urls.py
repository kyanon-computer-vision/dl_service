from django.urls import path
from .views import (
    VisionDatasetAPIView,
    VisionDatasetDetailAPIView,
    VisionDLModelAPIView,
    VisionDLModelDetailAPIView,
    CeleryAPIVIew,
    CheckProcessAPIView
)

urlpatterns = [
    path('datasets', VisionDatasetAPIView.as_view(), name='list'),
    path('datasets/<int:pk>', VisionDatasetDetailAPIView.as_view(), name='detail'),
    path('models', VisionDLModelAPIView.as_view(), name='list_models'),
    path('models/<int:pk>', VisionDLModelDetailAPIView.as_view(), name='detail_model'),
    path('models/train', CeleryAPIVIew.as_view()),
    path('checkprocess', CheckProcessAPIView.as_view())
    # path('models/<int:pk>/predict')
    # path('models/<int:pk>/)
]
