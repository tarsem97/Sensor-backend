from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from django.utils.timezone import now

class SensorDataPostAPIView(APIView):
    def post(self, request):
        device_id = request.data.get('device_id')

        if not device_id:
            return Response({'error': 'device_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get latest record for the device_id
            existing_data = SensorData.objects.filter(device_id=device_id).order_by('-timestamp').first()
            
            if existing_data:
                # Update the latest entry
                serializer = SensorDataSerializer(existing_data, data=request.data, partial=True)
            else:
                # Create a new entry
                serializer = SensorDataSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                response_data = serializer.data
                response_data.pop('device_id', None)  # remove device_id from response
                return Response(response_data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
            latest_data = SensorData.objects.filter(device_id=device_id).order_by('-timestamp').first()
            if latest_data:
                serialized = SensorDataSerializer(latest_data).data
                serialized.pop('device_id', None)
                serialized['sensor_name'] = label
                result.append(serialized)

        return Response(result, status=status.HTTP_200_OK)
