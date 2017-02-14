from crawlers import BaseWebCrawler
from parsers import ProductInfoParser


class ProductInfoWebCrawler(BaseWebCrawler):

    parser = ProductInfoParser

    def __init__(self, url):
        self.url = url
