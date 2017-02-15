from bs4 import BeautifulSoup

from exceptions import UnexpectedContentToParseException


class ProductInfoParser:

    @classmethod
    def parse(self, content):
        try:
            parsed = BeautifulSoup(content, 'html.parser')
            element = parsed.find('div', {'class': 'productName'})

            return {
                'name': element.attrs['class'][-2],
                'title': element.text,
            }
        except AttributeError:
            raise UnexpectedContentToParseException('Product Info Not Found - %s' % element)
