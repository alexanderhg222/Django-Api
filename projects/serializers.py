from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ['id', 'nombre', 'apellido', 'edad', 'fecha']
        read_only_fields=('fecha',)
