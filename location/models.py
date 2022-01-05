
from django.db import models

# Create your models here.


class LocationData(models.Model):
    # location,category,address
    location = models.TextField()
    category = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = 'location'

    def __str__(self):
        return f'{self.pk, self.location, self.category, self.address}'

