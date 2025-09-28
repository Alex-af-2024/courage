from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor
from .serializers import ActorSerializer


# Create your views here.
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer