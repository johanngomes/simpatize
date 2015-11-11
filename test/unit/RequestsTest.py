import unittest

from src.Requests import Requests


class RequestsTest(unittest.TestCase):

    def test_should_return_carrefour_when_searching_for_place_by_name(self):
        json = Requests.request_recife_metropolitan_area_places("carrefour")
        assert "carrefour" in json["results"][0]["name"].lower()

    def test_should_not_return_results_when_searching_for_inexistant_place_by_name(self):
        json = Requests.request_recife_metropolitan_area_places("no" * 8)
        assert "ZERO_RESULTS" in json["status"]

if __name__ == "__main__":
    unittest.main()
