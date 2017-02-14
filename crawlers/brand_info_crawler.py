from crawlers import BaseWebCrawler
from parsers import BrandInfoParser


class BrandInfoWebCrawler(BaseWebCrawler):

    parser = BrandInfoParser

    def __init__(self, url):
        self.url = url
