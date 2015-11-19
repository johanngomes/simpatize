from src.Requests import Requests


class SearchValidation:

    @staticmethod
    def validate_place_name(place_name):
        json = Requests.request_recife_metropolitan_area_places(place_name)

        if json["status"] == "ZERO_RESULTS":
            return "Estabelecimento não encontrado."

        return ""

