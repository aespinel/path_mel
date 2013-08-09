import datetime
from django.db import models

class ServerLog(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)
    action = models.IntegerField()
    entry_table = models.CharField(max_length=100)
    model_id = models.IntegerField(null = True)
