from django.shortcuts import render
from rest_framework import generics
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer