from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import main_clientsModel

class mainSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_clientsModel
        fields = ('client_id', 'client_name', 'client_county', 'client_age',)
