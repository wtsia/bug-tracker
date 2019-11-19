from rest_framework import serializers
from .models import Bugtracker

class BugtrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugtracker
        fields = ('id', 'title', 'description', 'completed')