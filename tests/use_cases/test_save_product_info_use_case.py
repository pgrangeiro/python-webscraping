from unittest.mock import patch

from use_cases import SaveProductInfoUseCase


class TestSaveProductInfoUseCase:

    def setup_method(self, test_method):
        self.patcher = patch('use_cases.save_product_info_use_case.ProductFactory', spec=True)
        self.factory = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_use_case_saves_product_correctly(self):
        '''
        product = {
            'name': 'Name',
            'title': 'Title',
            'url': 'http://xpto',
        }
        #TODO: Mock Behavior
        self.factory.create.return_value = Mock(**product)
        '''

        SaveProductInfoUseCase.execute('html content')
        self.factory.create.assert_called_once_with('html content')
