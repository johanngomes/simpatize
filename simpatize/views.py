from django.shortcuts import render

from src.PlaceHelper import PlaceHelper
from src.Requests import Requests
from src.SearchValidation import SearchValidation


def index(request):
    return render(request, "templates/index.html")


def search(request):

    place_name = request.GET["place_name"]

    message = SearchValidation.validate_place_name(place_name)

    if message["warning_message"] == "":
        json = Requests.request_recife_metropolitan_area_places(place_name)
        PlaceHelper.extract_places(json)
        return render(request, "templates/search.html",
                      {"places": PlaceHelper.places})
    else:
        return render(request, "templates/search.html", message)
