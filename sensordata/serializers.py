from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['device_id', 'temperature', 'humidity', 'timestamp']  # Include device_id in input
        read_only_fields = ['timestamp']

    def validate_device_id(self, value):
        """ Ensure the device_id is valid (one of the 4 choices). """
        if value not in ['device-1', 'device-2', 'device-3', 'device-4']:
            raise serializers.ValidationError("Invalid device_id. Must be one of: device-1, device-2, device-3, device-4.")
        return value

    def validate_temperature(self, value):
        """ Ensure temperature is a valid number. """
        if value is None:
            raise serializers.ValidationError("Temperature is required.")
        return value

    def validate_humidity(self, value):
        """ Ensure humidity is a valid number. """
        if value is None:
            raise serializers.ValidationError("Humidity is required.")
        return value
