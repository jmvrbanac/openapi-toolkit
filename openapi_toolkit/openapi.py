from collections import OrderedDict

from ruamel.yaml import add_representer, YAML
from ruamel.yaml.representer import RoundTripRepresenter

from openapi_toolkit.resolver import resolve_spec
from openapi_toolkit.schemas import validate_spec


class CustomRepresenter(RoundTripRepresenter):
    def ignore_aliases(self, _data):
        return True


class OpenAPI(object):
    def __init__(self, filename, spec):
        self.filename = filename
        self.spec = spec

    @classmethod
    def load(cls, filename, preprocessor=None, resolve=True, validate=True):
        with open(filename) as fp:
            raw = fp.read()

            if preprocessor:
                raw = preprocessor.handle(raw)

            yaml = YAML()
            yaml.Representer = CustomRepresenter
            data = yaml.load(raw)

            if resolve:
                data = resolve_spec(data)

            if validate:
                validate_spec(data)

            return cls(filename, data)

    def save(self, filename):
        with open(filename, 'w') as fp:
            # yaml.dump(self.spec, stream=fp, default_flow_style=False)
            yaml = YAML(typ='safe')
            yaml.default_flow_style = False
            yaml.Representer = CustomRepresenter
            yaml.dump(self.spec, stream=fp)
