import pytest

from unittest.mock import Mock, patch

from crawlers import BaseWebCrawler
from exceptions import BadRequestException


class TestBrandsWebCrawler:

    def setup_method(self, test_method):
        self.patcher = patch('crawlers.base_crawler.requests', spec=True)
        self.requests = self.patcher.start()

        stub_class = type('Stub', (BaseWebCrawler, ), {})
        self.crawler = stub_class()
        self.crawler.parser = Mock()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_execute_retuns_crawled_brands(self):
        self.crawler.parser.parse.return_value = [1, 2]
        response = Mock(status_code=200)
        self.requests.get.return_value = response
        self.requests.codes.ok = 200

        brands = self.crawler.execute()

        self.crawler.parser.parse.assert_called_once_with(response.content)
        assert [1, 2] == brands

    def test_execute_raises_exception_when_response_is_not_ok(self):
        self.requests.get.return_value = Mock(status_code=404)

        with pytest.raises(BadRequestException):
            self.crawler.execute()
