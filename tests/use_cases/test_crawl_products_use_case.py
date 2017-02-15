import pytest

from unittest.mock import patch

from use_cases import CrawlProductsUseCase


class TestCrawlProductsUseCase:

    def setup_method(self, test_method):
        self.patchers = [
            patch('use_cases.crawl_products_use_case.BrandsWebCrawler', spec=True),
            patch('use_cases.crawl_products_use_case.BrandInfoWebCrawler', spec=True),
            patch('use_cases.crawl_products_use_case.ProductsWebCrawler', spec=True),
            patch('use_cases.crawl_products_use_case.ProductInfoWebCrawler', spec=True),
        ]
        self.brands_crawler, self.brand_info_crawler, self.products_crawler, self.product_info_crawler = [p.start() for p in self.patchers]

    def teardown_method(self, test_method):
        [p.stop() for p in self.patchers]

    def test_execute_calls_crawlers_correctly(self):
        self.brands_crawler().execute.return_value = [{'url': 'brand_url'}]
        self.brand_info_crawler().execute.return_value = {'id': 1}
        self.products_crawler().execute.return_value = [{'id': 1, 'url': 'product_url'}]
        self.product_info_crawler().execute.return_value = {'name': 'Name', 'title': 'Title'}

        args = list(CrawlProductsUseCase.execute())

        self.brand_info_crawler.assert_called_with('brand_url')
        self.products_crawler.assert_called_with(1)
        self.product_info_crawler.assert_called_with('product_url')
        assert [(1, 'Name', 'Title', 'product_url')] == args

