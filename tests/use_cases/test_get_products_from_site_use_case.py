from unittest.mock import call, patch

from exceptions import BadRequestException, UnexpectedContentToParseException
from use_cases import GetProductsFromSiteUseCase


class TestGetProductsFromSiteUseCase:

    def setup_method(self, test_method):
        self.patchers = [
            patch('use_cases.get_products_from_site_use_case.CrawlProductsUseCase', spec=True),
            patch('use_cases.get_products_from_site_use_case.SaveProductInfoUseCase', spec=True),
            patch('use_cases.get_products_from_site_use_case.Logger', spec=True),
        ]
        self.crawler_uc, self.saveinfo_uc, self.logger = [p.start() for p in self.patchers]

    def teardown_method(self, test_method):
        [p.stop() for p in self.patchers]

    def test_execute_calls_use_cases_correctly(self):
        def side_effect():
            return [
                (1, 'name', 'title', 'url'),
                (2, 'Name', 'Title', 'Url'),
            ]
        self.crawler_uc.execute.side_effect = side_effect

        GetProductsFromSiteUseCase.execute()

        assert 2 == self.saveinfo_uc.execute.call_count
        self.saveinfo_uc.execute.assert_has_calls([call(name, title, url) for _id, name, title, url in side_effect()])

    def test_execute_calls_save_only_if_product_has_not_saved_before(self):
        def side_effect():
            return [
                (1, 'name', 'title', 'url'),
                (2, 'Name', 'Title', 'Url'),
                (1, 'name', 'title', 'url'),
            ]
        self.crawler_uc.execute.side_effect = side_effect

        GetProductsFromSiteUseCase.execute()

        assert 2 == self.saveinfo_uc.execute.call_count
        self.saveinfo_uc.execute.assert_has_calls([
            call('name', 'title', 'url'),
            call('Name', 'Title', 'Url'),
        ])

    def test_execute_calls_logger_when_unexpected_content_exception_raised(self):
        self.crawler_uc.execute.side_effect = UnexpectedContentToParseException('error')

        GetProductsFromSiteUseCase.execute()

        self.logger.log.assert_called_once_with('error')


    def test_execute_calls_logger_when_bad_request_exception_raised(self):
        self.crawler_uc.execute.side_effect = BadRequestException('error')

        GetProductsFromSiteUseCase.execute()

        self.logger.log.assert_called_once_with('error')
