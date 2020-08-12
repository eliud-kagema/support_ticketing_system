from django.conf import settings
from django.db import models
from django.utils import timezone


class Type(models.Model):
    type_name = models.CharField(max_length=50)
    added_by = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('inprogress', 'Inprogress'),
        ('closed', 'Closed'),
    )
    opened_by = models.CharField(max_length=100)
    opened_on = models.DateTimeField(default=timezone.now)
    closed_date = models.DateTimeField(null=True)
    office_description = models.CharField(null=True, max_length=100)
    ticket_type = models.ForeignKey(
        'Type',
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='pending')
    done_by = models.CharField(max_length=100)
    closed_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
