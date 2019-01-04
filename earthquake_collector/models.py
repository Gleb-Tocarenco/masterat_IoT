from django.db import models
from solo.models import SingletonModel


class SeismicRecord(models.Model):

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    device_id = models.CharField(max_length=255)
    amplitude = models.IntegerField(default=5)
    added_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'lat:{self.latitude} lon:{self.longitude} - {self.amplitude}'


class SeismicNotification(SingletonModel):

    amplitude = models.IntegerField(default=5)
