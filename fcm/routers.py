from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .api import DevicesViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'devices', DevicesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
