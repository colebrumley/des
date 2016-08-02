'''Configures logging'''

from logging import getLogger, Formatter, StreamHandler, INFO, DEBUG

GLOBAL_LOGGER = getLogger(__name__)
GLOBAL_LOGGER.setLevel(INFO)
SH = StreamHandler()
SH.setLevel(DEBUG)
FORMATTER = Formatter(
    '%(asctime)s - docker-event-script - %(levelname)s - %(message)s'
)
SH.setFormatter(FORMATTER)
GLOBAL_LOGGER.addHandler(SH)
