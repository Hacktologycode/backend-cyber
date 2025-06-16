from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.device_list),
    path('sessions/', views.session_list),
    path('red-team/', views.red_team_actions),
    path('blue-team/', views.blue_team_actions),
    path('alerts/', views.alert_list),
]