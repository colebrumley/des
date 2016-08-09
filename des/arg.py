'''Handle CLI args'''
from argparse import ArgumentParser
from des.__init__ import __version__

ARGPARSER = ArgumentParser(
    description='Run scripts in response to Docker events'
)

ARGPARSER.version = __version__

ARGPARSER.add_argument(
    '-c',
    '--create',
    dest='create',
    action='store_true',
    help='Create script dir structure and exit')

ARGPARSER.add_argument(
    '-e',
    dest='docker_url',
    action='store',
    default="unix:///var/run/docker.sock",
    help='Docker endpoint (Default: unix:///var/run/docker.sock)')

ARGPARSER.add_argument(
    '-d',
    dest='script_dir',
    action='store',
    default="/etc/docker/events.d",
    help='Event script directory')

ARGPARSER.add_argument(
    '-v',
    '--verbose',
    dest='verbose',
    action='store_true',
    help='Verbose output')

ARGPARSER.add_argument(
    '--version',
    dest='version',
    action='store_true',
    help='Print version and exit')
