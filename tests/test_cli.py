'''Testing the CLI functions'''

from .context import des

from unittest import TestCase
import mock

class TestCli(TestCase):
    def setUp(self):
        pass

    def test_write_script(self):
        loc = '/tmp/test'
        with mock.patch('des.cli.open', mock.mock_open()) as mocked_open:
            des.cli.write_script(loc)
            mocked_open.assert_called_once_with(loc, mode='x')
            handle = mocked_open()
            handle.write.assert_called_once_with('#!/bin/sh\n')
            handle.close.assert_called_once()

    @mock.patch('os.path.exists')
    def test_create_dirs_basedir_exists(self, mocked_exists):
        mocked_exists.return_value = True
        with self.assertRaises(OSError):
            des.cli.create_dirs('/test/dir')
