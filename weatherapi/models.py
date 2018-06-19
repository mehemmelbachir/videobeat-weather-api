from django.db import models


# Create your models here.
class InputData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    hight_ug = models.IntegerField()
    temperature = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_vector_direction = models.IntegerField()


class OutputData(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    avg_temperature = models.IntegerField()
    avg_wind_speed = models.IntegerField()
    direction_in_space = models.IntegerField()
