from django.db import models


class Place(models.Model):
    place_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    vicinity = models.CharField(max_length=200)







