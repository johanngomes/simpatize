from src.Requests import Requests


class SearchValidation:

    @staticmethod
    def validate_place_name(place_name):
        if place_name != "":
            json = Requests.request_recife_metropolitan_area_places(place_name)
        else:
            return {"warning_message": "Por favor, digite o nome do lugar que você deseja buscar."}

        if json["status"] == "ZERO_RESULTS":
            return {"warning_message": "Estabelecimento não encontrado."}

        return {"warning_message": ""}
