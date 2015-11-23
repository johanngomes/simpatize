from django.shortcuts import render
from django.http import JsonResponse
from src.RequestsGooglePlaces import RequestsGooglePlaces


def index(request):
    return render(request, "templates/info.html")


def search(request):

    place_name = request.GET["place_name"]
    place_type = request.GET["place_type"]
    nearby_places = request.GET["nearby_places"]

    request_result = RequestsGooglePlaces.request_recife_metropolitan_area_places(place_name, place_type)

    return JsonResponse(request_result["json"])
