"""Testing the Watcher class"""

from unittest import TestCase
import des
import mock

class TestWatcher(TestCase):
    def setUp(self):
        self.test_watcher = des.watcher.Watcher()

    def test_create(self):
        self.assertTrue(isinstance(self.test_watcher, des.watcher.Watcher))

    def test_watch(self):
        event_dicts = [
            dict(Type='container', Action='start'),
            dict(Type='container', Action='die'),
            dict(Type='network', Action='create'),
            ]

        clmock = mock.MagicMock()
        clmock.events.return_value = iter(event_dicts)
        self.test_watcher.client = clmock

        action = mock.MagicMock()
        self.test_watcher.wait_event(action)
        for d in mock.call.call_list():
            action.assert_called_with(d)

        # test failure cases
        with self.assertRaises(ValueError):
            self.test_watcher.wait_event(None)

        with self.assertRaises(RuntimeError):
            err_action = mock.MagicMock(side_effect=RuntimeError)
            self.test_watcher.wait_event(err_action())
