from django.shortcuts import render
from rest_framework import viewsets  # function to convert the data
from myapp.models import Task
from myapp.serializer import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
