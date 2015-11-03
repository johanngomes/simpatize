from pprint import pprint
from src.Place import Place


class PlaceHelper:

    places = []

    @staticmethod
    def add_place(place):
        PlaceHelper.places.append(place)

    @staticmethod
    def fill_places(json):
        PlaceHelper.places = []
        results = json["results"]
        for place in results:
            PlaceHelper.places.append(Place(place["name"], place["types"], place["vicinity"]))
