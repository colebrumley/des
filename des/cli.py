'''CLI entrypoint'''

from logging import DEBUG
from os import chmod, mkdir, path

from des.__init__ import EVENT_TYPES as type_list, __version__
from des.arg import ARGPARSER as parser
from des.log import GLOBAL_LOGGER as logger
from des.runner import ScriptRunner
from des.watcher import Watcher


def write_script(loc):
    '''Write an empty script to the filesystem'''
    logger.info('Creating script '+ loc)
    with open(loc, mode='x') as filehandle:
        filehandle.write('#!/bin/sh\n')
        filehandle.close()
        chmod(loc, 0o777)


def create_dirs(basedir):
    '''Create a generic script dir scaffold'''
    if path.exists(basedir):
        raise OSError(basedir+' exists!')

    mkdir(basedir)

    for key, event_ary in type_list.items():
        key_path = basedir+path.sep+key
        if not path.exists(key_path):
            mkdir(key_path)

        for event in event_ary:
            event_path = key_path+path.sep+event
            if not path.exists(event_path):
                write_script(event_path)


def main():
    '''Main CLI entrypoint for des'''
    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    if args.verbose:
        logger.setLevel(DEBUG)

    if args.create:
        logger.info('Creating template script directory at '+args.script_dir)
        create_dirs(args.script_dir)
        exit(0)

    watcher = Watcher()
    runner = ScriptRunner(args.script_dir)

    watcher.wait_event(runner.run)
