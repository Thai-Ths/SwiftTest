from rest_framework import routers

from .viewsets import EmailViewSet

app_name = "send"

router = routers.DefaultRouter()
router.register('mail', EmailViewSet)