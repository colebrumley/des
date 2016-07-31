"""Script Runner class"""

import os
import collections
from subprocess import STDOUT, check_output

from des.log import GLOBAL_LOGGER as logger


def flatten(parent_dict, parent_key='', sep='_'):
    '''Flatten a nested dict into a single layer'''
    items = []
    for key, val in parent_dict.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(val, collections.MutableMapping):
            items.extend(flatten(val, new_key, sep=sep).items())
        else:
            items.append((new_key, val))
    return dict(items)


class ScriptRunner(object):
    """Executes a script, passing event details via the ENV"""

    def __init__(self, path):
        self.basedir = path

    def run(self, event_dict):
        """Handle a docker event"""

        script = self.basedir + os.path.sep + event_dict['Type'] + \
                 os.path.sep + str(event_dict['Action']).split(':')[0]
        if os.path.exists(script):
            env_dict = dict()
            flat_event = flatten(event_dict)
            for key, val in flat_event.items():
                env_dict[str(key).upper()] = str(val)
            logger.info('Running script ' + script)
            logger.debug('Script ENV: ' + str(env_dict))
            result = check_output(
                script,
                stderr=STDOUT,
                env=env_dict
                )
            return str(result)
        else:
            logger.warning('Unable to handle event! No script exists at ' + script)

    def anotherfuncname(self, parameter_list):
        """Just to make the linter shut up"""
        raise NotImplementedError
