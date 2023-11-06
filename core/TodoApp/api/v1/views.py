from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from ...models import Task
from .serializers import TaskSerializers


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {'status':['exact', 'in']}
    ordering_fields = ['created_date']