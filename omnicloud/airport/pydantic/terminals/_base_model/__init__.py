from omnicloud.airport.abc import Building
from omnicloud.airport.tools.pkg import import_gates
from pydantic import BaseModel


class Terminal(BaseModel, Building):
    '''Omnicloud Airport Terminal for pydantic.BaseModel.'''

    @property
    def parcel(self):  # noqa: D102
        return self.dict()


import_gates(__file__, __name__)
