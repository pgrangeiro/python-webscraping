from crawlers import BaseWebCrawler
from parsers import BrandsParser


class BrandsWebCrawler(BaseWebCrawler):

    url = 'http://www.epocacosmeticos.com.br/marcas'
    parser = BrandsParser
