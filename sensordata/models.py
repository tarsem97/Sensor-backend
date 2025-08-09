from django.db import models

class SensorData(models.Model):
    DEVICE_CHOICES = [
        ('device-1', 'Device 1'),
        ('device-2', 'Device 2'),
        ('device-3', 'Device 3'),
        ('device-4', 'Device 4'),
    ]

    device_id = models.CharField(max_length=20, choices=DEVICE_CHOICES)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_id} | {self.temperature}°C | {self.humidity}%"
