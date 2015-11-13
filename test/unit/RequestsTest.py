import unittest

from src.Requests import Requests


class RequestsTest(unittest.TestCase):

    def test_should_return_carrefour_when_searching_for_place_by_name(self):
        json = Requests.request_recife_metropolitan_area_places("carrefour")
        assert "carrefour" in json["results"][0]["name"].lower()

if __name__ == "__main__":
    unittest.main()
