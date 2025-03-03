#poder llamar a un modelo especial de restframework
from rest_framework import serializers
#basado en un modelo que ya he creado. Django va a saber que responder ante put, post, delete...
from .models import Project

#convertir modelo en datos que pueden ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
            model = Project #modelo
            fields = ('id', 'title', 'description', 'technology', 'created_at') #campos
            read_only_fields = ('created_ad', ) #campos de solo lectura, no modificables
