from ruamel.yaml import YAML

from openapi_toolkit.resolver import resolve_spec
from openapi_toolkit.validator import validate_spec


def load(filename, preprocessor=None, resolve=True, validate=True):
    with open(filename) as fp:
        raw = fp.read()

        if preprocessor:
            raw = preprocessor.handle(raw)

        yaml = YAML(typ="safe")
        data = yaml.load(raw)

        if resolve:
            data = resolve_spec(data)

        if validate:
            validate_spec(data)

        return data
