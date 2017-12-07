from django.db import models
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'


# Create your models here.
class Computer(models.Model):
    READY = 'RD'
    WAITING = 'WT'
    PAPERWORK = 'PW'
    RESET = 'RS'
    CHOICES = (
        (WAITING, 'Waiting'),
        (READY, 'Ready'),
        (PAPERWORK, 'Paperwork'),
        (RESET, 'Reset'),
    )

    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    status = models.CharField(
        max_length=2,
        choices=CHOICES,
        default=WAITING,
    )

    def __str__(self):
        return self.name
