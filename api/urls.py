from django.urls import path,include
from rest_framework.routers import SimpleRouter

from .views import *

users_router = SimpleRouter(trailing_slash=False)
users_router.register(prefix='users',viewset=UserView,basename='users')

urlpatterns = [
    path('',include((users_router.urls,'Users API'),'api-users'))
]
