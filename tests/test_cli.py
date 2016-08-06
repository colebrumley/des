'''Testing the CLI functions'''

from .context import des

from unittest import TestCase
import mock

class TestCli(TestCase):
    def setUp(self):
        pass

    @mock.patch('os.path.exists')
    def test_create_dirs_basedir_exists(self, mocked_exists):
        mocked_exists.return_value = True
        with self.assertRaises(OSError):
            des.cli.create_dirs('/test/dir')
