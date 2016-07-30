"""Testing the CLI entrypoint"""

from unittest import TestCase
from des.cli import main

class TestCmd(TestCase):
    def test_basic(self):
        main()
