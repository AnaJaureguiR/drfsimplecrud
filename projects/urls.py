from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

#ruta + de donde coge los datos + nombre
router.register('api/projects', ProjectViewSet , 'projects')


urlpatterns = router.urls