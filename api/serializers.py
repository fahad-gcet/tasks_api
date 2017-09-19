from rest_framework import serializers

from api.models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', required=False)

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed', 'owner',)