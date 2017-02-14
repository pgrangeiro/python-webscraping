import pytest
import requests
import vcr

from exceptions import UnexpectedContentToParseException
from parsers import BrandInfoParser


class TestBrandInfoParser:

    @vcr.use_cassette('tests/fixtures/vcr/brand.yaml')
    def test_parse_content_returns_brands_info(self):
        response = requests.get('http://www.epocacosmeticos.com.br/1902')
        brand = BrandInfoParser.parse(response.content)

        assert {'id': '2000322'} == brand

    @vcr.use_cassette('tests/fixtures/vcr/error.yaml')
    def test_parse_raises_exception_when_content_has_no_expected_data(self):
        response = requests.get('http://google.com/')

        with pytest.raises(UnexpectedContentToParseException):
            BrandInfoParser.parse(response.content)
