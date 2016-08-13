Docker Event Scripts
===============================

[![CircleCI](https://circleci.com/gh/colebrumley/des.svg?style=svg)](https://circleci.com/gh/colebrumley/des)
[![codecov](https://codecov.io/gh/colebrumley/des/branch/master/graph/badge.svg)](https://codecov.io/gh/colebrumley/des)

version number: 0.1.0
author: Cole Brumley

Overview
--------

Run scripts in response to Docker events. See the Docker [docs](https://docs.docker.com/engine/reference/commandline/events/#/events) for the full list of possible scripts. Run `des -d SCRIPT_DIR -c` to generate a full dir structure with dummy scripts for every event. 

Installation / Usage
--------------------

To install use pip:

    $ pip install docker-event-scripts


Or clone the repo:

    $ git clone https://github.com/colebrumley/des.git
    $ python setup.py install
    
Contributing
------------

TBD

Example
-------

TBD
