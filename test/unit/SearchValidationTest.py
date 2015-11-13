import unittest
from src.SearchValidation import SearchValidation


class SearchValidationTest(unittest.TestCase):

    def test_should_return_warning_message_for_nonexistent_place(self):
        message = SearchValidation.validate_place_name("aaaaaaaaaaaaaaaaaaaaaa")
        assert message["warning_message"] == "Estabelecimento não encontrado."

    def test_should_return_warning_message_when_search_field_is_empty(self):
        message = SearchValidation.validate_place_name("")
        assert message["warning_message"] == "Por favor, digite o nome do lugar que você deseja buscar."

    def test_should_return_empty_warning_message_for_existent_place_name(self):
        message = SearchValidation.validate_place_name("carrefour")
        assert message["warning_message"] == ""


if __name__ == "__main__":
    unittest.main()