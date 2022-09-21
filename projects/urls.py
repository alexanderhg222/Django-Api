from rest_framework import routers
from .api import ViewProject

router=routers.DefaultRouter()
router.register('api/project',ViewProject,'projects')

urlpatterns =router.urls