"""Testing the ScriptRunner class"""

from unittest import TestCase
import des

class TestRunner(TestCase):
    def test_create(self):
        test_runner = des.runner.ScriptRunner()
        self.assertTrue(isinstance(test_watcher, des.runner.ScriptRunner())
