from django.db import models


class PlaceKind(models.Model):
    kind = models.CharField(max_length=200)


class Place(models.Model):
    name = models.CharField(max_length=200)
    kind = models.ForeignKey(PlaceKind)
    likes = models.IntegerField(default=0)


# Place.objects.update_or_create(name="ThoughtWorks")
# Place.objects.update_or_create(name="Sushi Digital")
# Place.objects.update_or_create(name="Clube Metrópole")

# PlaceKind.get_or_create()

