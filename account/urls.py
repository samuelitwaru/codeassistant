from codeassistant import router
from django.urls import path, include
from account.views import UserViewSet

router.register(r'users', UserViewSet)
