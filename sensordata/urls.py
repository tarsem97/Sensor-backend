from django.urls import path
from .views import SensorDataPostAPIView, SensorDataGetAPIView

urlpatterns = [
    path('create-sensor/', SensorDataPostAPIView.as_view(), name='sensor-data-post'),
    path('get-sensor/', SensorDataGetAPIView.as_view(), name='sensor-data-get'),
]