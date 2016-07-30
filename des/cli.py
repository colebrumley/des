"""CLI entrypoint"""

from logging import DEBUG

from des.arg import ARGPARSER as parser
from des.log import GLOBAL_LOGGER as logger
from des.runner import ScriptRunner
from des.watcher import Watcher


def main():
    """Enter here"""
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(DEBUG)

    watcher = Watcher()
    runner = ScriptRunner(args.script_dir)

    watcher.wait_event(runner.run)
