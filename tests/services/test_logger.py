from unittest.mock import patch

from services import Logger


class TestLogger:

    def setup_method(self, test_method):
        self.patcher = patch('services.logger.logging')
        self.logging = self.patcher.start()

    def teardown_method(self, test_method):
        self.patcher.stop()

    def test_log_calls_logging_lib_correctly(self):
        Logger.log('msg')

        self.logging.basicConfig.assert_called_with(filename='error.log')
        self.logging.error.assert_called_once_with('msg')
