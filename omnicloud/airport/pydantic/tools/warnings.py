'''Module contains custom warnings classes.'''


class DocumentExistsWarning(Warning):
    '''You try to create a document that already exists.

    An attempt to save the data if the corresponding document exists and overwrite it is allowed.
    '''

    def __init__(self, path: str, **kw):  # noqa: D107
        self.path = path
        self.message = f'The document {path} was be overwritten!'
        super().__init__(self.message, **kw)
