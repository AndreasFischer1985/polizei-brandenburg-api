"""
    Polizei Brandenburg API

    Nachrichten, Hochwasser-, Verkehrs- und Waldbrandwarnungen der Polizei Brandenburg  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.polizei_brandenburg.model.news_data import NewsData

from deutschland import polizei_brandenburg

globals()["NewsData"] = NewsData
from deutschland.polizei_brandenburg.model.news import News


class TestNews(unittest.TestCase):
    """News unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNews(self):
        """Test News"""
        # FIXME: construct object with mandatory attributes with example values
        # model = News()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
