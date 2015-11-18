import unittest

from selenium import webdriver


class IndexTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_simpatize_on_page_title(self):
        self.driver.get("http://localhost:8000/")
        print(self.driver.title)
        assert "Simpatize" in self.driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

