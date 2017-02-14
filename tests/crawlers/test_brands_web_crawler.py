import pytest

from unittest.mock import Mock, patch

from crawlers import BrandsWebCrawler
from exceptions import BadRequestException


class TestBrandsWebCrawler:

    def setup_method(self, test_method):
        self.patchers = [
            patch('crawlers.brands.BrandsParser', spec=True),
            patch('crawlers.brands.requests', spec=True),
        ]
        self.parser, self.requests = [p.start() for p in self.patchers]

    def teardown_method(self, test_method):
        [p.stop() for p in self.patchers]

    def test_execute_retuns_crawled_brands(self):
        self.parser.parse.return_value = [1, 2]
        response = Mock(status_code=200)
        self.requests.get.return_value = response
        self.requests.codes.ok = 200

        brands = BrandsWebCrawler.execute()

        self.parser.parse.assert_called_once_with(response.content)
        assert [1, 2] == brands

    def test_execute_raises_exception_when_response_is_not_ok(self):
        self.requests.get.return_value = Mock(status_code=404)

        with pytest.raises(BadRequestException):
            BrandsWebCrawler.execute()
