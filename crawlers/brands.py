import requests

from exceptions import BadRequestException
from parsers import BrandsParser


class BrandsWebCrawler:

    url = 'http://www.epocacosmeticos.com.br/marcas'

    @classmethod
    def execute(cls):
        response = requests.get(cls.url)

        if response.status_code != requests.codes.ok:
            raise BadRequestException

        return BrandsParser.parse(response.content)
