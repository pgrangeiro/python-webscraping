from bs4 import BeautifulSoup

from exceptions import UnexpectedContentToParseException


class ProductInfoParser:

    @classmethod
    def parse(self, content):
        try:
            parsed = BeautifulSoup(content, 'html.parser')
            wrapper = parsed.find('h1', {'itemprop': 'name'})
            element = wrapper.find('div', {'class': 'productName'})

            return {
                'name': element.attrs['class'][-2],
                'title': element.text,
            }
        except AttributeError:
            raise UnexpectedContentToParseException
