from django.shortcuts import render

from src.PlaceHelper import PlaceHelper
from src.Requests import Requests


def index(request):
    return render(request, "templates/index.html")


def search(request):
    json = Requests.request_recife_metropolitan_area_places(request.GET["place_name"])

    if json["status"] == "ZERO_RESULTS":
        return render(request, "templates/search.html",
                      {"place_not_found": "Lugar nao encontrado!"})
    else:
        PlaceHelper.extract_places(json)
        return render(request, "templates/search.html",
                      {"places": PlaceHelper.places})
