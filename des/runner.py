"""Script Runner class"""

import os
from subprocess import STDOUT, check_output

from des.log import GLOBAL_LOGGER as logger


class ScriptRunner(object):
    """Executes a script, passing event details via the ENV"""

    def __init__(self, path):
        self.basedir = path

    def run(self, event_dict):
        """Handle a docker event"""

        script = self.basedir + os.path.sep + event_dict['Type'] + \
                 os.path.sep + event_dict['Action']
        if os.path.exists(script):
            logger.debug('Running script ' + script)
            result = check_output(
                script,
                stderr=STDOUT,
                env=event_dict
                )
            return str(result)
        else:
            logger.warning('Unable to handle event! No script exists at ' + script)

    def anotherfuncname(self, parameter_list):
        """Just to make the linter shut up"""
        raise NotImplementedError
