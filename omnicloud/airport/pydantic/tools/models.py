'''Helper functions for pydantic.BaseModel.'''

from omnicloud.airport.tools.dict import enrich as _enrich
from omnicloud.airport.tools.dict import item_converter as _converter


__all__ = ['parameters', 'kw4dict']


parameters = {
    'dict': [
        'include',
        'exclude',
        'by_alias',
        'skip_defaults',
        'exclude_unset',
        'exclude_defaults',
        'exclude_none',
    ]
}


def kw4dict(options: dict, name4log: str | None = None) -> dict:
    '''Prepare **kw to pydantic.BaseModel.dict() function.

    Args:
        options: Passed arguments.
        name4log: The name that will be used for logging. Default: name of the function.

    Returns:
        Prepared arguments as dictionary
    '''
    if not name4log:
        name4log = kw4dict.__name__

    kwargs = {}

    for k in parameters['dict']:
        kwargs = _enrich(kwargs, options, k)

    kwargs = _converter(kwargs, 'exclude_none', bool, name4log)
    kwargs = _converter(kwargs, 'exclude_defaults', bool, name4log)
    kwargs = _converter(kwargs, 'exclude_unset', bool, name4log)
    kwargs = _converter(kwargs, 'skip_defaults', bool, name4log)
    kwargs = _converter(kwargs, 'by_alias', bool, name4log)

    return kwargs
