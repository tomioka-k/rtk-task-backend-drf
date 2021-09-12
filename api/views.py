from rest_framework import permissions
from .serializers import UserSerializers, TaskSerializers
from .models import Task
from django.contrib.auth.models import User

from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )


class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers