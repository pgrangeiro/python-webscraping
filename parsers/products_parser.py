from bs4 import BeautifulSoup


class ProductsParser:

    @classmethod
    def parse(self, content):
        parsed = BeautifulSoup(content, 'html.parser')
        wrapper = parsed.find_all('li')

        for element in wrapper:
            product = element.find('a', {'class': 'productImage'})
            if product:
                yield {
                    'id': element.find('span', {'class': 'product-data-id'}).text,
                    'url': product.attrs['href'],
                }
