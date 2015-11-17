import requests

from simpatize.settings import GOOGLE_PLACES_API_KEY


class Requests:

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

        return requests.get(url).json()
