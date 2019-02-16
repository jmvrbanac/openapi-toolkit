from ruamel.yaml import YAML

from openapi_toolkit.resolver import resolve_spec
from openapi_toolkit.validator import validate_spec


def load(filename, resolve=True, validate=True):
    with open(filename) as fp:
        yaml = YAML(typ="safe")
        data = yaml.load(fp)

        if resolve:
            data = resolve_spec(data)

        if validate:
            validate_spec(data)

        return data
