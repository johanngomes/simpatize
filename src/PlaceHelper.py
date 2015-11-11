from simpatize.models import Place


class PlaceHelper:

    places = []

    @staticmethod
    def extract_places(json):

        PlaceHelper.places = []
        results = json["results"]

        for place in results:
            PlaceHelper.places.append(Place.objects.create(
                place_id=place["id"], name=place["name"], types=place["types"], vicinity=place["vicinity"])
            )
