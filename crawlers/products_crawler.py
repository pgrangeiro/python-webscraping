from crawlers import BaseWebCrawler
from parsers import ProductsParser


class ProductsWebCrawler(BaseWebCrawler):

    parser = ProductsParser

    def __init__(self, brand_id):
        self.url = 'http://www.epocacosmeticos.com.br/buscapagina?fq=B:%s&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=' % brand_id
