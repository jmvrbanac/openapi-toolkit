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


def test_saving_resolved_spec(spec, tmpdir):
    tmp_path = str(tmpdir.join('test.yml'))
    spec.save(tmp_path)

    # Make sure all refs have been resolved
    assert '$ref' not in tmpdir.join('test.yml').read()

    # Reload to make sure it generated validate data
    OpenAPI.load(tmp_path)
