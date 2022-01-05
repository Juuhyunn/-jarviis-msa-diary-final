from datetime import datetime

from django.db import models

# Create your models here.


class UserLog(models.Model):
    location = models.TextField(null=True)
    address = models.TextField(null=True)
    x = models.TextField(null=True)
    y = models.TextField(null=True)
    log_date = models.DateTimeField(default=datetime.now())
    weather = models.TextField(null=True)
    log_type = models.TextField(null=True)
    contents = models.TextField()
    event_id = models.IntegerField(null=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'userlog'

    def __str__(self):
        return f"{self.pk}"