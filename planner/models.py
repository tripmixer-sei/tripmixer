from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Destination(models.Model):
    holiday = models.ForeignKey(Holiday,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.name