import pytest

from openapi_toolkit.resolver import get_node


def test_get_node_invalid_path():
    spec = {}

    with pytest.raises(KeyError) as err:
        get_node('/thing/doesnt/exist', spec)

    assert err.value.args[0] == 'Cannot resolve /thing/doesnt/exist'
