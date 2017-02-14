from crawlers import BaseWebCrawler, ProductsWebCrawler
from parsers import ProductsParser


class TestProductsWebCrawler:

    def test_instantiates_obj_correctly(self):
        crawler = ProductsWebCrawler('url')

        assert 'http://www.epocacosmeticos.com.br/buscapagina?fq=B:url&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=' == crawler.url
        assert ProductsParser == crawler.parser
        assert isinstance(crawler, BaseWebCrawler)

