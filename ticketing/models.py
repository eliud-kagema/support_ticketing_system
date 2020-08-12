from django.conf import settings
from django.db import models
from django.utils import timezone


class Type(models.Model):
    type_name = models.CharField(max_length=50)
    added_by = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name
