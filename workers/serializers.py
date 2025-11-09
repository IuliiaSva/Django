from rest_framework import serializers
from .models import Worker
from workplaces.models import Workplaces

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'skills', 'grade', 'description', 'workplace']

class WorkplacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplaces
        fields = ['id', 'number']
