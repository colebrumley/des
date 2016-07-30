"""Testing the Watcher class"""

from unittest import TestCase
import des

class TestWatcher(TestCase):
    def test_create(self):
        test_watcher = des.watcher.Watcher()
        self.assertTrue(isinstance(test_watcher, des.watcher.Watcher)
