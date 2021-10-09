from src.scraper import news
import unittest


class TestMethods(unittest.TestCase):
    def test_len(self):
        scrapper = news()
        response = scrapper.getNews("bitcoin",5)
        assert len(response) == 5


if __name__ == "__main__":
    unittest.main()

    
# python -m unittest test.test
