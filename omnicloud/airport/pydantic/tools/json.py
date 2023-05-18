'''Tools for serializing Pydantic models to JSON.'''

from datetime import datetime as dt
from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from json import JSONEncoder


class StringEncoder(JSONEncoder):
    '''Custom JSON encoder for pydantic models.

    Provides features for encoding IP addresses and formatted datetimes.

    Default datetime format is '%Y-%m-%d %H:%M:%S' This format is compatible with Google Firestore.
    For using another format you can override dt_format class attribute.
    '''

    dt_format = '%Y-%m-%d %H:%M:%S'

    def default(self, o):  # noqa: D102
        match o:
            case dt():
                return o.strftime(self.dt_format)
            case Enum():
                return o.value
            case IPv4Address() | IPv6Address():
                return o.compressed

            case _:
                return JSONEncoder.default(self, o)
