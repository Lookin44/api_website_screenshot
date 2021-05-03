from rest_framework import serializers

from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tasks
