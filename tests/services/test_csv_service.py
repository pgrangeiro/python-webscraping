from unittest.mock import mock_open, patch

from services import CSVService


class TestCSVService:

    def setup_method(self, test_method):
        self.mopen = mock_open()
        self.patcher = patch('services.csv_service.csv', spec=True)
        self.mcsv = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_save_content_in_file_correctly(self):
        with patch('services.csv_service.open', self.mopen):
            CSVService.write('name', 'title', 'url')

            self.mopen.assert_called_once_with('output.csv', 'w', newline='')
            self.mcsv.writer.assert_called_once_with(self.mopen())
            self.mcsv.writer().writerow.assert_called_once_with(('name', 'title', 'url'))
