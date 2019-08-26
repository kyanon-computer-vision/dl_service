from django.urls import path
from .views import VisionDatasetAPIView, VisionDatasetDetailAPIView

urlpatterns = [
    path('datasets', VisionDatasetAPIView.as_view(), name='list'),
    path('datasets/<int:pk>', VisionDatasetDetailAPIView.as_view(), name='detail')
]
