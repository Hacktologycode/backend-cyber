# core/serializers.py
from rest_framework import serializers
from .models import Device, Session, RedTeamAction, BlueTeamAction, Alert

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class RedTeamActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedTeamAction
        fields = '__all__'

class BlueTeamActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlueTeamAction
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'