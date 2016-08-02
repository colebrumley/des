'''Watcher Class definition'''

import os
from datetime import datetime

# from docker import Client
import docker
from des.log import GLOBAL_LOGGER as logger


class Watcher(object):
    '''Docker daemon monitor object'''

    def __init__(self,
                 endpoint='unix:///var/run/docker.sock',
                 http_timeout=10,
                 api_version='auto',
                 tls_config=None):

        self.endpoint = endpoint
        self.client = docker.Client(
            base_url=endpoint,
            version=api_version,
            timeout=http_timeout,
            tls=tls_config)

    def wait_event(self, action):
        '''Wait for events'''

        if not callable(action):
            raise ValueError

        logger.info("watching " + self.endpoint + " for container events")
        for event in self.client.events(since=datetime.utcnow(), decode=True):
            event_key = event['Type'] + os.path.sep + event['Action']
            logger.debug("Detected actionable event " + event_key + ": " + str(event))
            try:
                output = action(event)
                logger.debug('Finished handling ' + event_key)
                if output:
                    logger.debug("SCRIPT OUTPUT: " + str(output))
            except RuntimeError as err:
                logger.error('Failed to execute task in reponse to "' +
                             event_key + '" :' + str(err))
