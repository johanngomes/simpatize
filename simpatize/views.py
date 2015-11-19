from django.shortcuts import render

from src.PlaceHelper import PlaceHelper
from src.RequestsGooglePlaces import RequestsGooglePlaces


def index(request):
    return render(request, "templates/index.html")


def search(request):

    place_name = request.GET["place_name"]
    place_type = request.GET["place_type"]
    nearby_places = request.GET["nearby_places"]

    request_result = RequestsGooglePlaces.request_recife_metropolitan_area_places(place_name, place_type)

    PlaceHelper.extract_places(request_result["json"])

    return render(request, "templates/search.html",
                  {"places": PlaceHelper.places,
                   "warning_message": request_result["warning_message"]})
