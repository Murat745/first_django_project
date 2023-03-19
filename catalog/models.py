from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Stuff(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    stuff = models.ManyToManyField(Stuff)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
