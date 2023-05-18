from pydantic import BaseModel, Extra


class CamelModel(BaseModel):
    '''This class provides allies_generator function in Config subclass.

    Thanks to it all properties name in OpenAPI will be had an allies in camel format.
    For example: if BaseModel property has name example_name you can use this name in
    python code, but OpenAPI specification will be contains field ExampleName.
    '''

    class Config:  # noqa: D106
        @staticmethod
        def alias_generator(name) -> str:  # noqa: D102
            return ''.join(word.capitalize() for word in name.split('_'))


class NoAdditional(BaseModel):
    '''This class sets the additionalProperties property of JSON schema to False.

    By default JSON parsers validate only objects defined in the schema. If additionalProperties
    set to False parsers raise an exception if document contains don't defined objects.
    '''

    class Config:  # noqa: D106
        extra = Extra.forbid
