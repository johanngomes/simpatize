from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from src.PlaceHelper import PlaceHelper
from src.Requests import Requests


def index(request):
    template = loader.get_template("templates/index.html")
    return HttpResponse(template.render())


def search(request):
    json = Requests.request_recife_metropolitan_area_places(request.GET["place_name"])

    PlaceHelper.fill_places(json)

    return render(request, "templates/search.html", {"places": PlaceHelper.places})
