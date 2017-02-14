from crawlers import BaseWebCrawler, BrandsWebCrawler
from parsers import BrandsParser


class TestBrandsWebCrawler:

    def test_instantiates_obj_correctly(self):
        crawler = BrandsWebCrawler()

        assert 'http://www.epocacosmeticos.com.br/marcas' == crawler.url
        assert BrandsParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

