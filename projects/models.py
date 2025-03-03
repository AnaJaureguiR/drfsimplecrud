from django.db import models

# Create your models here. Esto crea las tablas en bbdd y declaramos sus columnas con su tipo.
class Project (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)