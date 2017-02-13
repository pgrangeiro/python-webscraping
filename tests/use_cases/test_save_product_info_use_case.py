from unittest.mock import Mock, patch

from domain import Product
from use_cases import SaveProductInfoUseCase


class TestSaveProductInfoUseCase:

    def setup_method(self, test_method):
        self.patcher = patch('use_cases.save_product_info_use_case.ProductFactory', spec=True)
        self.factory = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_use_case_saves_product_correctly(self):
        data = {
            'name': 'Name',
            'title': 'Title',
            'url': 'http://xpto',
        }
        instance = Mock(Product, **data)
        self.factory.create.return_value = instance

        SaveProductInfoUseCase.execute('html content')
        self.factory.create.assert_called_once_with('html content')
        instance.save.assert_called_once_with()
