from unittest.mock import call, Mock, patch

from crawlers import BaseWebCrawler, ProductsWebCrawler
from parsers import ProductsParser


class TestProductsWebCrawler:

    def setup_method(self, test_method):
        self.patcher = patch('crawlers.base_crawler.requests', spec=True)
        self.requests = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_instantiates_obj_correctly(self):
        crawler = ProductsWebCrawler('url')

        assert 'http://www.epocacosmeticos.com.br/buscapagina?fq=B:url&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=1' == crawler.url
        assert ProductsParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

    def test_next_page_changes_current_page_attr(self):
        crawler = ProductsWebCrawler('url')
        assert 1 == crawler.current_page

        crawler.next_page()
        assert 2 == crawler.current_page

    def test_execute_change_page_when_crawled_all_products_from_current_page(self):
        crawler = ProductsWebCrawler('url')
        crawler.parser = Mock(crawler.parser)
        crawler.parser.parse.side_effect = ([1, 2], [])

        response = Mock(status_code=200)
        self.requests.get.return_value = response
        self.requests.codes.ok = 200

        products = list(crawler.execute())

        assert 2 == self.requests.get.call_count
        self.requests.get.has_calls([
            call('http://www.epocacosmeticos.com.br/buscapagina?fq=B:url&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=1'),
            call('http://www.epocacosmeticos.com.br/buscapagina?fq=B:url&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=2'),
        ])
        assert [1, 2] == products

