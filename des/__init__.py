'''Set the version'''

__version__ = '0.1.3'

EVENT_TYPES = {
    'container': ['attach', 'commit', 'copy', 'create', 'destroy',
                  'detach', 'die', 'exec_create', 'exec_detach',
                  'exec_start', 'export', 'kill', 'oom', 'pause',
                  'rename', 'resize', 'restart', 'start', 'stop',
                  'top', 'unpause', 'update'],
    'image': ['delete', 'import', 'load', 'pull',
              'push', 'save', 'tag', 'untag'],
    'volume': ['create', 'mount', 'unmount', 'destroy'],
    'network': ['create', 'connect', 'disconnect', 'destroy'],
    'daemon': ['reload']
}
