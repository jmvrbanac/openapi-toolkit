API Documentation
=================

.. autoclass:: openapi_toolkit.OpenAPI
   :members:

.. autoclass:: openapi_toolkit.JsonSchema
   :members:

.. function:: openapi_toolkit.schema_format

    Decorator to add custom JSONSchema format checkers

    e.g.

    .. code-block:: python

        @schema_format.checks('uuid', ValueError)
        def uuid_format(value):
            return uuid.UUID(value)

.. autoclass:: openapi_toolkit.MakoPreprocessor
   :members:
