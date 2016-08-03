"""Testing the Watcher class"""

from unittest import TestCase
import des

class TestWatcher(TestCase):
    def setUp(self):
        self.test_watcher = des.watcher.Watcher()

    def test_create(self):
        self.assertTrue(isinstance(self.test_watcher, des.watcher.Watcher))
