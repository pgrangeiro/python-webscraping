from unittest.mock import call, patch

from use_cases import GetProductsFromSiteUseCase


class TestGetProductsFromSiteUseCase:

    def setup_method(self, test_method):
        self.patchers = [
            patch('use_cases.get_products_from_site_use_case.CrawlProductsUseCase'),
            patch('use_cases.get_products_from_site_use_case.SaveProductInfoUseCase'),
        ]
        self.crawler_uc, self.saveinfo_uc = [p.start() for p in self.patchers]

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
        self.saveinfo_uc.has_calls([call(p) for p in side_effect()])

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
        self.saveinfo_uc.has_calls([
            call(1, 'name', 'title', 'url'),
            call(2, 'Name', 'Title', 'Url'),
        ])

