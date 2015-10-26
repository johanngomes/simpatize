import unittest

from selenium import webdriver


class IndexTest(unittest.TestCase):

    def test_simpatize_on_page_title(self):
        driver = webdriver.Firefox()
        driver.get("http://localhost:8000/")
        assert "Simpatize" in driver.title
        driver.close()


if __name__ == "__main__":
    unittest.main()


