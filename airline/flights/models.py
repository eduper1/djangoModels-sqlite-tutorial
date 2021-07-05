from django.db import models

# Create your models here.
class Airports(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="Arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
class Passenger (models.Model):
    first = models.CharField(max_length=64 )
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passenger")
    
    def __str__(self):
        return f"{self.first} {self.last}"
    