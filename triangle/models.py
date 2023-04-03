from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class Logs(models.Model):
    CHOICES = (
        ('CONNECT', 'CONNECT'),
        ('DELETE', 'DELETE'),
        ('GET', 'GET'),
        ('HEAD', 'HEAD'),
        ('OPTIONS', 'OPTIONS'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
    )
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=7, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.method} {self.timestamp} {self.data}'
