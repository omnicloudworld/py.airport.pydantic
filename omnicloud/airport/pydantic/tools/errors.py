'''Module contains custom exceptions classes.'''


class DocumentExistsError(Exception):
    '''You try to create a document that already exists.

    An attempt to save the data if the corresponding document exists and overwrite is not allowed.
    '''

    def __init__(self, path: str, **kw):  # noqa: D107
        self.path = path
        self.message = f'The document {path} already exists and overwriting is not allowed!'
        super().__init__(self.message, **kw)


class DocumentDontExistError(Exception):
    '''You try to read a document that doesn't exists.

    An attempt to read the data if the corresponding document doesn't exists.
    '''

    def __init__(self, path: str, **kw):  # noqa: D107
        self.path = path
        self.message = f'The document {path} already doesn\'t exists!'
        super().__init__(self.message, **kw)


class UnknownTypeError(Exception):
    '''An attempt to read or write didn't allow file type.'''

    def __init__(self, file: str, **kw):  # noqa: D107
        self.file = file
        self.message = f'The file {file} is a disallowed type.'
        super().__init__(self.message, **kw)
