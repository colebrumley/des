"""Testing the Watcher class"""

from unittest import TestCase

import mock

from .context import des


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

        mock_docker_client = mock.MagicMock()
        mock_docker_client.events.return_value = iter(event_dicts)
        self.test_watcher.client = mock_docker_client

        action = mock.MagicMock()
        self.test_watcher.wait_event(action)
        action.assert_has_calls([mock.call(d) for d in event_dicts], any_order=True)

        # test failure cases
        with self.assertRaises(ValueError):
            self.test_watcher.wait_event(None)

        with self.assertRaises(RuntimeError):
            err_action = mock.MagicMock(side_effect=RuntimeError)
            self.test_watcher.wait_event(err_action())
