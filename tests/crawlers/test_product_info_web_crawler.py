from crawlers import BaseWebCrawler, ProductInfoWebCrawler
from parsers import ProductInfoParser


class TestProductInfoWebCrawler:

    def test_instantiates_obj_correctly(self):
        crawler = ProductInfoWebCrawler('url')

        assert 'url' == crawler.url
        assert ProductInfoParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

