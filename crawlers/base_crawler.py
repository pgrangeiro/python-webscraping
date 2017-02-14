from abc import ABCMeta
import requests

from exceptions import BadRequestException


class BaseWebCrawler:

    __metaclass__ = ABCMeta

    url = ''
    parser = None

    def execute(self):
        response = requests.get(self.url)

        if response.status_code != requests.codes.ok:
            raise BadRequestException

        return self.parser.parse(response.content)
