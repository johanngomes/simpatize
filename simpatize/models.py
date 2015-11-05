from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    vicinity = models.CharField(max_length=200)





