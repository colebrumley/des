'''Script Runner class'''

from os.path import sep, exists
from subprocess import STDOUT, CalledProcessError, check_output

from des.log import GLOBAL_LOGGER as logger
from des.util import flatten


class ScriptRunner(object):
    '''Executes a script, passing event details via the ENV'''

    def __init__(self, path):
        self.basedir = path

    def script_exec(self, script, envarg):
        '''Actually execute the script/command'''
        try:
            result = check_output(
                script,
                stderr=STDOUT,
                env=envarg,
                shell=True)
            return result
        except CalledProcessError as err:
            logger.error('Script '+script+' Failed! Exit='+ \
                         str(err.returncode)+' Message="'+str(err.output)+'"')

    def build_env(self, event):
        '''Translate the event dict into environment variables'''
        env_dict = dict()
        for key, val in flatten(event).items():
            env_dict[str(key).upper()] = str(val)
        return env_dict

    def run(self, event_dict):
        '''Handle a docker event'''

        script = self.basedir + sep + event_dict.get('Type') + \
                 sep + str(event_dict.get('Action')).split(':')[0]

        if exists(script) == False:
            logger.warning('Unable to handle event! No script exists at ' + script)
            return
        
        env_dict = self.build_env(event_dict)

        logger.info('Running script ' + script)
        logger.debug('Script ENV: ' + str(env_dict))
        self.script_exec(script, env_dict)
