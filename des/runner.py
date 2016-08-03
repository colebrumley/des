'''Script Runner class'''

import os
from subprocess import STDOUT, CalledProcessError, check_output

from des.log import GLOBAL_LOGGER as logger
from des.util import flatten


class ScriptRunner(object):
    '''Executes a script, passing event details via the ENV'''

    def __init__(self, path):
        self.basedir = path

    def run(self, event_dict):
        '''Handle a docker event'''

        script = self.basedir + os.path.sep + event_dict['Type'] + \
                 os.path.sep + str(event_dict['Action']).split(':')[0]
        if os.path.exists(script):
            env_dict = dict()
            flat_event = flatten(event_dict)
            for key, val in flat_event.items():
                env_dict[str(key).upper()] = str(val)
            logger.info('Running script ' + script)
            logger.debug('Script ENV: ' + str(env_dict))
            try:
                result = check_output(
                    script,
                    stderr=STDOUT,
                    env=env_dict,
                    shell=True)
                return str(result)
            except CalledProcessError as err:
                logger.error('Script '+script+' Failed! Exit='+ \
                             str(err.returncode)+' Message="'+str(err.output)+'"')
        else:
            logger.warning('Unable to handle event! No script exists at ' + script)
