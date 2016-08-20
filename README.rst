Docker Event Scripts
===============================

*Run scripts in response to Docker events.*

.. image:: https://circleci.com/gh/colebrumley/des.svg?style=svg
.. image:: https://codecov.io/gh/colebrumley/des/branch/master/graph/badge.svg

**Version**: 0.1.3
**Author**: Cole Brumley

Overview
--------

Use the ``des`` command to monitor `Docker <https://docker.com>`_ for events. When an event occurs, ``des`` executes a script with the event metadata exported to the environment.

Installation / Usage
--------------------

To install use pip:

    pip install docker-event-scripts

The script directory is defined via the ``-d`` flag, and defaults to ``/etc/docker/events.d``. Scripts should be placed in sub-directories in the format ``SCRIPT_DIR/EVENT_TYPE/EVENT`` and should be marked executable.

The environment variables set during each script run are a flattened version of the raw API event dictionary. If you're writing a script for an event you're unfamiliar with, you may want to run it once with ``printenv`` to see what's available.

See the Docker `docs <https://docs.docker.com/engine/reference/commandline/events/#/events>`_
for the full list of possible events.

To generate a full directory structure with dummy scripts for every event, run ``des -c``.

Contributing
------------

Please submit issues or pull requests via the `GitHub repo <https://github.com/colebrumley/des>`_.


Example
-------

Using the default script directory, when this example container was started using ``docker run -it --rm alpine sh``, the script at ``/etc/docker/events.d/container/start`` was executed with the following environment:


    ACTION=start
    ACTOR_ATTRIBUTES_IMAGE=alpine
    TIME=1471131434
    ACTOR_ID=467730e17a0ac265eae034d21cf633755aa57d03483ae479b623bc5569d6c274
    STATUS=start
    ACTOR_ATTRIBUTES_NAME=backstabbing_lichterman
    ID=467730e17a0ac265eae034d21cf633755aa57d03483ae479b623bc5569d6c274
    FROM=alpine
    TYPE=container
    TIMENANO=1471131434853322607

