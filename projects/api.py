#con esto vamos a manejar quien puede mandar peticiones y que tipo de peticiones de serializers.py
from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet (viewsets.ModelViewSet):
   queryset =  Project.objects.all() #consulta todos los datos de una tabla
   permission_classes = [permissions.AllowAny] #cualquier aplicación cliente va a poder solicitar datos. se podría cambiar por ver si está logeado, etc.
   serializer_class = ProjectSerializer