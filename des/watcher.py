"""Watcher Class definition"""

from datetime import datetime

# from docker import Client
import docker
import os
from des.log import GLOBAL_LOGGER as logger


class Watcher(object):
    """Docker daemon monitor object"""

    def __init__(self,
                 endpoint='unix:///var/run/docker.sock',
                 http_timeout=30,
                 api_version='auto',
                 use_tls=False,
                 tls_client_cert=None,
                 tls_client_key=None,
                 tls_ca=None,
                 tls_version=1.2,
                 tls_verify=True,
                 tls_check_hostname=False):

        self.tls_config = False

        if use_tls:
            crt = None
            if tls_client_cert and tls_client_key:
                crt = (tls_client_cert, tls_client_key)
            elif tls_client_cert:
                crt = (tls_client_cert)

            self.tls_config = docker.tls.TLSConfig(
                client_cert=crt,
                verify=tls_verify,
                ssl_version=tls_version,
                assert_hostname=tls_check_hostname,
                ca_cert=tls_ca)

        self.endpoint = endpoint
        self.client = docker.Client(
            base_url=endpoint,
            version=api_version,
            timeout=http_timeout,
            tls=self.tls_config)

    def wait_event(self, action):
        """Wait for events"""

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

    def anotherfuncname(self, parameter_list):
        """Just to make the linter shut up"""
        raise NotImplementedError
