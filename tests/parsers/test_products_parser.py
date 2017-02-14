import requests
import vcr

from parsers import ProductsParser


class TestProductsParser:

    @vcr.use_cassette('tests/fixtures/vcr/products.yaml')
    def test_parse_content_returns_brands_info(self):
        response = requests.get('http://www.epocacosmeticos.com.br/buscapagina?fq=B%3a2000435&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=1')
        products = list(ProductsParser.parse(response.content))

        assert 5 == len(products)
        assert {'id': '11063', 'url': 'http://www.epocacosmeticos.com.br/protetor-solar-facial-fps60-actsun-protetor-solar/p'} in products
        assert {'id': '11065', 'url': 'http://www.epocacosmeticos.com.br/protetor-solar-facial-fps45-actsun-protetor-solar/p'} in products
