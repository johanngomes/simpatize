import requests

from simpatize.settings import GOOGLE_PLACES_API_KEY
from src.SearchValidation import SearchValidation
from src.Constants import Constants


class RequestsGooglePlaces:

    @staticmethod
    def request_recife_metropolitan_area_places(place_name="", types=""):
        latitude = "-8.0475622"
        longitude = "-34.8769643"
        radius = "20000"
        types = types
        name = place_name
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" \
            "location={},{}&radius={}&types={}&name={}&key={}".format(latitude, longitude,
                                                                        radius, types, name,
                                                                        GOOGLE_PLACES_API_KEY)

        json = requests.get(url).json()

        return RequestsGooglePlaces.format_request_result(json)

    @staticmethod
    def format_request_result(json):
        if SearchValidation.is_zero_results(json):
            return {"json": json, "warning_message": Constants.WARNING_PLACE_NOT_FOUND}
        else:
            return {"json": json, "warning_message": ""}

