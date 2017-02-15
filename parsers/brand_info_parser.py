import re

from bs4 import BeautifulSoup

from exceptions import UnexpectedContentToParseException


class BrandInfoParser:

    @classmethod
    def parse(self, content):
        try:
            parsed = BeautifulSoup(content, 'html.parser')
            wrapper = parsed.find(text=re.compile('"brandId:[0-9]{7}'))
            return {
                'id': wrapper[wrapper.find('brandId:'):-6].replace('brandId:', '')
            }
        except AttributeError:
            raise UnexpectedContentToParseException('Brand Info Not Found - %s' % wrapper)
