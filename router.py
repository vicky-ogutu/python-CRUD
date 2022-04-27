from rest_framework import routers
from CRUD_operation.viewsets import mainViewsets

router = routers.DefaultRouter()
router.register('clients', mainViewsets)
