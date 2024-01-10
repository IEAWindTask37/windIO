import yaml
import os
from pathlib import Path
import jsonschema
import json
from urllib.parse import urljoin
import xarray as xr


class Loader(yaml.SafeLoader):

    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]

        super().__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f, self.__class__)

Loader.add_constructor('!include', Loader.include)

class XrResourceLoader(Loader):

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.yaml', '.yml']:
            with open(filename, 'r') as f:
                return yaml.load(f, XrResourceLoader)
        elif ext in ['.nc']:
            def fmt(v):
                if isinstance(v, dict):
                    return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
                elif isinstance(v, tuple):
                    return list(v)
                else:
                    return v

            def ds2yml(ds):
                d = ds.to_dict()
                return fmt({**{k: v['data'] for k, v in d['coords'].items()},
                            **d['data_vars']})
            return ds2yml(xr.open_dataset(filename))


XrResourceLoader.add_constructor('!include', XrResourceLoader.include)


def load_yaml(filename, loader=XrResourceLoader):
    if isinstance(filename, dict):
        return filename  # filename already yaml dict
    with open(filename) as fid:
        return yaml.load(fid, loader)


def validate_yaml(data_file, schema_file, loader=XrResourceLoader):

    def add_local_schemas_to(resolver, schema_folder, base_uri, schema_ext_lst=['.json', '.yaml', '.yml']):
        '''Function from https://gist.github.com/mrtj/d59812a981da17fbaa67b7de98ac3d4b#file-local_ref-py
        Add local schema instances to a resolver schema cache.

        Arguments:
            resolver (jsonschema.RefResolver): the reference resolver
            schema_folder (str): the local folder of the schemas.
            base_uri (str): the base URL that you actually use in your '$id' tags
                in the schemas
            schema_ext (str): filter files with this extension in the schema_folder
        '''
        for dir, _, files in os.walk(schema_folder):
            for file in files:
                if Path(file).suffix in schema_ext_lst:
                    schema_path = Path(dir) / Path(file)
                    rel_path = schema_path.relative_to(schema_folder)
                    try:
                        with open(schema_path) as schema_file:
                            if schema_path.suffix == '.json':
                                schema_doc = json.load(schema_file)
                            if schema_path.suffix in ['.yml', '.yaml']:
                                schema_doc = yaml.safe_load(schema_file)

                        key = urljoin(base_uri, str(rel_path))
                        resolver.store[key] = schema_doc
                    # except (ScannerError, ParserError):
                    except Exception:
                        print("Reading %s failed" % file)

    data = load_yaml(data_file, loader)
    schema = load_yaml(schema_file)

    schema_folder = Path(schema_file).parent
    base_uri = 'https://www.example.com/schemas/'

    resolver = jsonschema.RefResolver(base_uri=base_uri, referrer=schema)
    add_local_schemas_to(resolver, schema_folder, base_uri)
    jsonschema.validate(data, schema, resolver=resolver)

    print("Validation succeeded")
