from ...models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "status", "created_date"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["status"] = instance.get_status_display()
        return representation
