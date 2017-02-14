import pytest
import requests
import vcr

from exceptions import UnexpectedContentToParseException
from parsers import BrandsParser


class TestBrandsParser:

    @vcr.use_cassette('tests/fixtures/vcr/brands.yaml')
    def test_parse_content_returns_brands_info(self):
        response = requests.get('http://www.epocacosmeticos.com.br/marcas')
        brands = list(BrandsParser.parse(response.content))

        assert 404 == len(brands)
        assert {'name': '1902', 'url': 'http://www.epocacosmeticos.com.br/1902'} in brands
        assert {'name': 'Vizeme', 'url': 'http://www.epocacosmeticos.com.br/vizeme'} in brands

    @vcr.use_cassette('tests/fixtures/vcr/error.yaml')
    def test_parse_raises_exception_when_content_has_no_expected_data(self):
        response = requests.get('http://google.com/')

        with pytest.raises(UnexpectedContentToParseException):
            list(BrandsParser.parse(response.content))
