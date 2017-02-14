from crawlers import BaseWebCrawler, ProductsWebCrawler
from parsers import ProductsParser


class TestProductsWebCrawler:

    def test_instantiates_obj_correctly(self):
        crawler = ProductsWebCrawler('url')

        assert 'url' == crawler.url
        assert ProductsParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

