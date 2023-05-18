from omnicloud.airport.terminals import Dict
from omnicloud.airport.abc import Gate

from .. import Terminal

__all__ = ['LocalJSON']


class LocalJSON(Terminal.Gate):
    @classmethod
    def arriving(cls, place: str, **options):  # noqa: D102
        option_string = ','.join([f'{k}={v}' for k, v in options.items()])
        data = Dict.arriving(f'LocalJSON::{place}::{option_string}')

        return Terminal.validate(data)

    @classmethod
    def departure(cls, parcel, place: str, **options):
        option_string = ','.join([f'{k}={v}' for k, v in options.items()])
        Dict.departure(parcel, f'LocalJSON::{place}::{option_string}')
