from crawlers import BaseWebCrawler, BrandInfoWebCrawler
from parsers import BrandInfoParser


class TestBrandInfoWebCrawler:

    def test_instantiates_obj_correctly(self):
        crawler = BrandInfoWebCrawler('url')

        assert 'url' == crawler.url
        assert BrandInfoParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

