# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device, Session, RedTeamAction, BlueTeamAction, Alert
from .serializers import DeviceSerializer, SessionSerializer, RedTeamActionSerializer, BlueTeamActionSerializer, AlertSerializer

@api_view(['GET', 'POST'])
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST', 'PATCH'])
def session_list(request):
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def red_team_actions(request):
    if request.method == 'GET':
        actions = RedTeamAction.objects.all()
        serializer = RedTeamActionSerializer(actions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RedTeamActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def blue_team_actions(request):
    if request.method == 'GET':
        actions = BlueTeamAction.objects.all()
        serializer = BlueTeamActionSerializer(actions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlueTeamActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST', 'PATCH'])
def alert_list(request):
    if request.method == 'GET':
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)