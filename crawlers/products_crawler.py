from crawlers import BaseWebCrawler
from parsers import ProductsParser


class ProductsWebCrawler(BaseWebCrawler):

    parser = ProductsParser

    def __init__(self, brand_id):
        self.base_url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=B:%s&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=' % brand_id
        self.current_page = 1

    def next_page(self):
        self.current_page += 1

    @property
    def url(self):
        return '%s%s' % (self.base_url, self.current_page)

    def execute(self):
        products = list(super(ProductsWebCrawler, self).execute())

        while products:
            for product in products:
                yield product
            self.next_page()
            products = list(super(ProductsWebCrawler, self).execute())

