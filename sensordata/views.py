from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from random import choice

class SensorDataPostAPIView(APIView):
    def post(self, request):
        # Make sure device_id is passed in the request body
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the sensor data including device_id
            # Exclude device_id from the response by returning only temperature, humidity, and timestamp
            response_data = serializer.data
            response_data.pop('device_id', None)  # Remove device_id from the response data
            return Response(response_data, status=status.HTTP_201_CREATED)  # Send response without device_id
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDataGetAPIView(APIView):
    def get(self, request):
        # Mapping device_id to readable names
        sensor_labels = {
            'device-1': 'sensor 1',
            'device-2': 'sensor 2',
            'device-3': 'sensor 3',
            'device-4': 'sensor 4',
        }

        result = []

        for device_id, label in sensor_labels.items():
            device_data = SensorData.objects.filter(device_id=device_id)
            if device_data.exists():
                random_entry = choice(device_data)
                serialized = SensorDataSerializer(random_entry).data
                serialized.pop('device_id', None)
                serialized['sensor_name'] = label  # 👈 Add 'sensor 1', etc.
                result.append(serialized)

        return Response(result)
