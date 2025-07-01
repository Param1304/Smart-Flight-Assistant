# myapp/models.py
from django.db import models
class FlightDelayPrediction(models.Model):
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    month = models.IntegerField()
    hour = models.IntegerField()
    is_weekend = models.BooleanField()
    day_of_month = models.IntegerField()
    day_of_week = models.IntegerField()
    prediction_result = models.FloatField()  # Assuming your predict_delay() returns a numeric delay time or probability
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.airline} | {self.origin} -> {self.destination} | Predicted Delay: {self.prediction_result}"
