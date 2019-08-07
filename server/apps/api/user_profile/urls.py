from django.conf.urls import include, url
from .views import ProfileRetrieveAPIView

urlpatterns = [
    url('profiles/<string:username>', ProfileRetrieveAPIView.as_view())
]
