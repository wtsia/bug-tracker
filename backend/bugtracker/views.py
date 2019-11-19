from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BugtrackerSerializer
from .models import Bugtracker

class BugtrackerView(viewsets.ModelViewSet):
    serializer_class = BugtrackerSerializer
    queryset = Bugtracker.objects.all()