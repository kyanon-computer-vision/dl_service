from django.conf.urls import url
from .views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    url('registration/', RegistrationAPIView.as_view()),
    url('auth/', LoginAPIView.as_view()),
]