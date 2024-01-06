from codeassistant import router
from django.urls import path, include
from .views import *

router.register(r'models', ModelViewSet)
router.register(r'fields', FieldViewSet)
