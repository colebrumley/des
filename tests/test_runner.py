'''Testing the ScriptRunner class'''

import os
from sys import getdefaultencoding
from unittest import TestCase

# import mock
from .context import des


class TestRunner(TestCase):
    def setUp(self):
        self.test_runner = des.runner.ScriptRunner('/tmp')

    def test_create(self):
        '''Make sure that TestRunneris in fact a TestRunner'''
        self.assertTrue(isinstance(self.test_runner, des.runner.ScriptRunner))

    def test_build_env(self):
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

    def test_exec(self):
        '''Test execution'''
        result = self.test_runner.script_exec('/usr/bin/printenv', {'ENV_VAR_1': 'env_val_1'})
        self.assertEqual(result, bytes('ENV_VAR_1=env_val_1\nPWD='+ os.getcwd() +'\n',
                                       getdefaultencoding()))
