Welcome to Docker Event Scripts's documentation!
=========================================

Usage
==================
Yes the usage section is just the help output::

    usage: des [-h] [-c] [-e DOCKER_URL] [-d SCRIPT_DIR] [-v] [--version]

    Run scripts in response to Docker events

    optional arguments:
    -h, --help     show this help message and exit
    -c, --create   Create script dir structure and exit
    -e DOCKER_URL  Docker endpoint (Default: unix:///var/run/docker.sock)
    -d SCRIPT_DIR  Event script directory
    -v, --verbose  Verbose output
    --version      Print version and exit

Scripts
==================
Scripts are run based on the structure of the script directory, in the format ``SCRIPT_DIR/<event_type>/<action>``, where ``event_type`` is one of container, daemon, image, network, or volume. The full list of possible event type and action combinations can be found in the `docker docs`_.

Scripts should be marked executable and should not have an extension. Invoking the CLI with the ``-c`` flag will generate a template directory with dummy scripts for every event type.

Each script has the API event object serialized into the environment. Nested objects are joined with underscores. Below is a container start event as a JSON blob from the API and below that the same object as environment vars:: 

    {
        "Action": "create",
        "id": "4e70ce9c8025f0627eb1e1a7c3cf85131dce984e336a8c066670597e54ae476a",
        "timeNano": 1470184049299521300,
        "status": "create",
        "from": "alpine",
        "time": 1470184049,
        "Type": "container",
        "Actor": {
            "Attributes": {
                "image": "alpine",
                "name": "jovial_wilson"
            },
            "ID": "4e70ce9c8025f0627eb1e1a7c3cf85131dce984e336a8c066670597e54ae476a"
        }
    }

    ACTION=create
    ID=4e70ce9c8025f0627eb1e1a7c3cf85131dce984e336a8c066670597e54ae476a
    TIMENANO=1470184049299521300
    STATUS=create
    FROM=alpine
    TIME=1470184049
    TYPE=container
    ACTOR_ATTRIBUTES_IMAGE=alpine
    ACTOR_ATTRIBUTES_NAME=jovial_wilson
    ACTOR_ID=4e70ce9c8025f0627eb1e1a7c3cf85131dce984e336a8c066670597e54ae476a

Different event types export different information, so a good first step is to run a ``printenv`` script on that event to familiarize yourself with what's available.

.. _docker docs: https://docs.docker.com/engine/reference/commandline/events/#/events 

Running as a Service
==================
See the ``contrib/`` folder for a systemd init script. More flavors will be added as the PRs roll in ;) 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

