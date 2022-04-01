"""
RedisMQ
"""

import os
import logging

__version__ = "1.1.0"

_log = logging.getLogger(__name__)

from .debugging import create_log_handler

create_log_handler(_log, level=os.getenv("REDISMQ", logging.WARNING))

from .client import Client
from .producer import Producer
from .consumer import Consumer
from .publisher import Publisher
from .subscriber import Subscriber

__all__ = ["Client", "Producer", "Consumer", "Publisher", "Subscriber"]
