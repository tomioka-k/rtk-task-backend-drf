from api.views import TaskViewSet
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import CreateUserView, MyProfileView, TaskViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
  path('myself/', MyProfileView.as_view(), name="myself"),
  path('register/', CreateUserView.as_view(), name="register"),
  path('', include(router.urls)),
]
