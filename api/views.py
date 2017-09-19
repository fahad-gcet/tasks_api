from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Task
from api.serializers import TaskSerializer

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer