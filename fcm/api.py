from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import DeviceSerializer
from .utils import get_device_model

Device = get_device_model()


class DevicesViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'delete', 'options', 'get']
