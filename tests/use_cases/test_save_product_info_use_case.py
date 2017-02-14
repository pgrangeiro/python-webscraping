from unittest.mock import patch

from use_cases import SaveProductInfoUseCase


class TestSaveProductInfoUseCase:

    def test_use_case_saves_product_correctly(self):
        mocked = patch('use_cases.save_product_info_use_case.Product', spec=True).start()
        data = {
            'name': 'Name',
            'title': 'Title',
            'url': 'http://xpto',
        }

        SaveProductInfoUseCase.execute(**data)
        mocked.assert_called_once_with('Name', 'Title', 'http://xpto')
        mocked().save.assert_called_once_with()
