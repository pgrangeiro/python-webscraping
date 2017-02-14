from crawlers import BaseWebCrawler
from parsers import ProductsParser


class ProductsWebCrawler(BaseWebCrawler):

    parser = ProductsParser

    def __init__(self, url):
        self.url = url
