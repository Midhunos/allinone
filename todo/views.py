from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from todo.serializers import TaskSerializer
from todo.models import ToDo

# Create your views here.

class CreateTodo(ListCreateAPIView):
    queryset=ToDo.objects.all()
    serializer_class=TaskSerializer

class GetUpdate(RetrieveUpdateDestroyAPIView):
     queryset=ToDo.objects.all()
     serializer_class=TaskSerializer

