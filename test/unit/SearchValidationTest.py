import unittest

from src.SearchValidation import SearchValidation
from src.RequestsGooglePlaces import RequestsGooglePlaces


class SearchValidationTest(unittest.TestCase):

    def test_should_return_warning_message_for_nonexistent_place(self):
        request_result = RequestsGooglePlaces.request_recife_metropolitan_area_places("a" * 20)
        assert SearchValidation.is_zero_results(request_result['json']) is True

    def test_should_not_return_any_warning_message_for_existent_place(self):
        request_result = RequestsGooglePlaces.request_recife_metropolitan_area_places("carrefour" * 20)
        assert SearchValidation.is_zero_results(request_result['json']) is False

if __name__ == "__main__":
    unittest.main()