from bs4 import BeautifulSoup

from exceptions import UnexpectedContentToParseException


class BrandsParser:

    @classmethod
    def parse(self, content):
        try:
            parsed = BeautifulSoup(content, 'html.parser')
            wrapper = parsed.find('div', {'class': 'brandFilter'})

            for element in wrapper.find_all('a'):
                yield {
                    'name': element.text,
                    'url': element.attrs['href'],
                }
        except AttributeError:
            raise UnexpectedContentToParseException
