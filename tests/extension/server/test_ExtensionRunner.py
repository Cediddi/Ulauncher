import os
import pytest
import mock
from time import sleep
from ulauncher.extension.server.ExtensionRunner import ExtensionRunner


class TestExtensionRunner:

    @pytest.fixture
    def extensions_dir(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__)))

    @pytest.fixture
    def runner(self, extensions_dir):
        runner = ExtensionRunner()
        runner.extensions_dir = extensions_dir
        return runner

    @pytest.fixture(autouse=True)
    def logger(self, mocker):
        logging = mocker.patch('ulauncher.extension.server.ExtensionRunner.logging')
        return logging.getLogger.return_value

    def test_run__logs__are_captured(self, runner, logger):
        runner.run('test_extension')
        logger.info.assert_called_with('test')
