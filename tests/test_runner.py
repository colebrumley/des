'''Testing the ScriptRunner class'''

import os
from sys import getdefaultencoding
from unittest import TestCase

import mock

from .context import des


class TestRunner(TestCase):
    def setUp(self):
        self.test_runner = des.runner.ScriptRunner('/tmp')

    def test_create(self):
        '''Make sure that TestRunner is in fact a TestRunner'''
        self.assertTrue(isinstance(self.test_runner, des.runner.ScriptRunner))

    def test_build_env_dict_translation(self):
        '''Test docker event to environment dict translation'''
        event_dict = {
            'status': 'start',
            'Type': 'container',
            'Actor': {
                'Attributes': {
                    'Name': 'test-01',
                    'Image': 'alpine'
                }
            }
        }

        anticipated_result = {
            'STATUS': 'start',
            'TYPE': 'container',
            'ACTOR_ATTRIBUTES_NAME': 'test-01',
            'ACTOR_ATTRIBUTES_IMAGE': 'alpine'
        }

        result = self.test_runner.build_env(event_dict)
        self.assertDictEqual(result, anticipated_result)

    def test_script_exec_handles_good_scripts(self):
        '''Test good executions'''
        expected_output = bytes('ENV_VAR_1=env_val_1\nPWD='+ \
                                os.getcwd() +'\n', getdefaultencoding())

        result = self.test_runner.script_exec('/usr/bin/printenv',
                                             {'ENV_VAR_1': 'env_val_1'})

        self.assertEqual(result, expected_output)

    def test_script_exec_handles_script_errors(self):
        '''Test bad executions'''
        self.assertIsNone(self.test_runner.script_exec('/bin/false', {}))

    def test_run_handles_missing_scripts(self):
        '''Test missing scripts'''
        event = dict(Type='missing', Action='file')
        self.assertIsNone(self.test_runner.run(event))
    
    def test_run_handles_existing_scripts(self):
        '''Test existing scripts'''
        self.test_runner.basedir = ''
        event = dict(Type='bin', Action='true')
        exec_mock = mock.MagicMock()
        self.test_runner.script_exec = exec_mock
        self.assertIsNone(self.test_runner.run(event))
        exec_mock.assert_called_once_with('/bin/true', {'TYPE': 'bin', 'ACTION': 'true'})
