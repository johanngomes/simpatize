import unittest

from src.RequestsGooglePlaces import RequestsGooglePlaces


class RequestsTest(unittest.TestCase):

    def test_should_return_carrefour_when_searching_for_place_by_name(self):
        request_results = RequestsGooglePlaces.request_recife_metropolitan_area_places("carrefour")
        assert "carrefour" in request_results["json"]["results"][0]["name"].lower()

    def test_should_return_recife_international_airport_when_place_name_is_aeroporto_internacional_and_place_type_is_aeroporto(self):
        request_results = RequestsGooglePlaces.request_recife_metropolitan_area_places("aeroporto internacional", "airport")
        assert "recife international airport" in request_results["json"]["results"][0]["name"].lower() and \
               len(request_results["json"]["results"]) is 1

    def test_should_return_more_than_one_place_when_place_name_is_aeroporto_internacional_and_place_type_is_not_selected(self):
        request_results = RequestsGooglePlaces.request_recife_metropolitan_area_places("aeroporto internacional")
        assert len(request_results["json"]["results"]) > 1

if __name__ == "__main__":
    unittest.main()
