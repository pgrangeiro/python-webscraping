from unittest.mock import patch
from domain import Product


class TestProduct:

    def setup_method(self, test_method):
        self.patcher = patch('domain.product.CSVService', spec=True)
        self.service = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_instantiates_obj_correctly(self):
        instance = Product('name', 'title', 'url')
        assert 'name' == instance.name
        assert 'title' == instance.title
        assert 'url' == instance.url

    def test_save_calls_service_correctly(self):
        instance = Product('name', 'title', 'url')
        instance.save()

        self.service.write.assert_called_once_with('name', 'title', 'url')
