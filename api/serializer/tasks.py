from rest_framework import serializers
from ..model.tasks import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task', 'is_complete', 'type', 'user']
        
    def create(self, validated_data):
        user = validated_data.get('user')
        task = Task(
            task=validated_data.get('task'),
            is_complete=validated_data.get('is_complete'),
            type=validated_data.get('type'),
            user=user
        )
        task.save()
        return task