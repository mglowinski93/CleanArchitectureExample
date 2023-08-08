from django.db import models


class Template(models.Model):
    id = models.UUIDField(primary_key=True)
    value = models.TextField()
    timestamp = models.DateTimeField()
