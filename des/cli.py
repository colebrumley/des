'''CLI entrypoint'''

from logging import DEBUG
from os import chmod, mkdir, path

from des.__init__ import EVENT_TYPES as type_list
from des.arg import ARGPARSER as parser
from des.log import GLOBAL_LOGGER as logger
from des.runner import ScriptRunner
from des.watcher import Watcher


def create_dirs(basedir):
    '''Create a generic script dir scaffold'''
    if not path.exists(basedir):
        mkdir(basedir)
    for key, event_ary in type_list.items():
        key_path = basedir+path.sep+key
        if not path.exists(key_path):
            mkdir(key_path)
        for event in event_ary:
            event_path = key_path+path.sep+event
            logger.info('Creating script '+ event_path)
            if not path.exists(event_path):
                with open(event_path, mode='x') as fh:
                    fh.write('#!/bin/sh\n')
                    fh.close()
                    chmod(event_path, 0o777)


def main():
    '''Main CLI entrypoint for des'''
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(DEBUG)

    if args.create:
        logger.info('Creating template script directory at '+args.script_dir)
        create_dirs(args.script_dir)
        exit(0)

    watcher = Watcher()
    runner = ScriptRunner(args.script_dir)

    watcher.wait_event(runner.run)
