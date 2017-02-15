from abc import ABCMeta
import requests

from exceptions import BadRequestException, UnexpectedContentToParseException


class BaseWebCrawler:

    __metaclass__ = ABCMeta

    url = ''
    parser = None

    def execute(self):
        response = requests.get(self.url)

        if response.status_code != requests.codes.ok:
            raise BadRequestException('Unavailable url - %s' % self.url)

        try:
            return self.parser.parse(response.content)
        except UnexpectedContentToParseException as e:
            raise UnexpectedContentToParseException('%s - %s' % (e.message, self.url))
