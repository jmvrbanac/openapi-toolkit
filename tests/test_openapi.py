import os

import pytest

from openapi_toolkit import OpenAPI

sample_path = os.path.join(os.path.dirname(__file__), 'sample_spec.yml')


@pytest.fixture
def spec():
    yield OpenAPI.load(sample_path)


def test_loading_openapi(spec):
    quote_path = spec.find_path('/quote')
    assert hasattr(quote_path, 'get')
    assert hasattr(quote_path, 'post')

    input_schema = spec.find_input_schema('/quote', 'post', 'application/json')
    assert input_schema == {
        'type': 'object',
        'properties': {
            'quote': {'type': 'string'},
            'author': {'type': 'string'}
        },
        'required': ['quote', 'author'],
    }
