import unittest
from src.SearchValidation import SearchValidation


class SearchValidationTest(unittest.TestCase):

    def test_should_return_warning_message_for_nonexistent_place(self):
        assert SearchValidation.validate_place_name("a" * 20) == "Estabelecimento não encontrado."

    def test_should_not_return_any_warning_message_for_existent_place(self):
        assert SearchValidation.validate_place_name("carrefour") == ""

if __name__ == "__main__":
    unittest.main()