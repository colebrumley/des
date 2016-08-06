"""Testing the Watcher class"""

from unittest import TestCase

import mock

from .context import des


class TestWatcher(TestCase):
    def setUp(self):
        self.event_dicts = [
            dict(Type='container', Action='start'),
            dict(Type='container', Action='die'),
            dict(Type='network', Action='create'),
            ]

        self.test_watcher = des.watcher.Watcher()
        mock_docker_client = mock.MagicMock()
        mock_docker_client.events.return_value = iter(self.event_dicts)
        self.test_watcher.client = mock_docker_client

    def test_create_watcher(self):
        self.assertTrue(isinstance(self.test_watcher, des.watcher.Watcher))

    def test_watch_events_passes_events_to_action(self):
        action = mock.MagicMock()
        self.test_watcher.wait_event(action)
        action.assert_has_calls([mock.call(d) for d in self.event_dicts], any_order=True)

    def test_watch_events_ensure_callable(self):
        with self.assertRaises(ValueError):
            self.test_watcher.wait_event(None)

    def test_watch_events_handle_runtime_error(self):
        err_action = mock.MagicMock(side_effect=RuntimeError)
        self.assertIsNone(self.test_watcher.wait_event(err_action))
