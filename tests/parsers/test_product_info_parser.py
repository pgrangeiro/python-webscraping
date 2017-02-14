import pytest
import requests
import vcr

from exceptions import UnexpectedContentToParseException
from parsers import ProductInfoParser


class TestProductInfoParser:

    @vcr.use_cassette('tests/fixtures/vcr/product.yaml')
    def test_parse_content_returns_brands_info(self):
        response = requests.get('http://www.epocacosmeticos.com.br/hair-touch-up-l-oreal-professionnel-corretivo-instantaneo/p')
        product = ProductInfoParser.parse(response.content)
        assert 'Hair-Touch-Up-L’Oreal-Professionnel---Corretivo-Instantaneo-75ml' == product['name']
        assert 'Hair Touch Up L’Oréal Professionnel - Corretivo Instantâneo 75ml' == product['title']

    @vcr.use_cassette('tests/fixtures/vcr/error.yaml')
    def test_parse_raises_exception_when_content_has_no_expected_data(self):
        response = requests.get('http://google.com/')

        with pytest.raises(UnexpectedContentToParseException):
            list(ProductInfoParser.parse(response.content))
