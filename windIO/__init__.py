
from __future__ import annotations
import yaml
import os
import copy
from pathlib import Path, PosixPath, WindowsPath
import jsonschema
import json
from urllib.parse import urljoin
import xarray as xr
from typing import Any
import re

### API design
import windIO.examples.plant
import windIO.examples.turbine
import windIO.schemas
import windIO.schemas.plant         # By importing plant and turbine here, we can use the schemas as windIO.schemas.plant and windIO.schemas.turbine
import windIO.schemas.turbine       # in the calling code after only importing windIO... import windIO; help(windIO.schemas.turbine)

plant_ex = windIO.examples.plant
turbine_ex = windIO.examples.turbine
schemas = windIO.schemas
### API design


class XrResourceLoader(yaml.SafeLoader):
    """
    This class is a custom loader for yaml files that also enables loading
    NetCDF files. For pure YAML files, it behaves like the default yaml.SafeLoader.
    For NetCDF files, it uses xarray to load the data and then converts it to a dictionary.
    Software incorporating windIO generally will not need to use this class directly.
    """
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super().__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.yaml', '.yml']:
            with open(filename, 'r') as f:
                return yaml.load(f, XrResourceLoader)
        elif ext in ['.nc']:
            def fmt(v: Any) -> dict | list | str | float | int:
                """
                Formats a dictionary appropriately for yaml.load by converting Tuples to Lists.

                Args:
                    v (Any): Initially, a dictionary of inputs to format. Then, individual
                        values within the dictionary.
                """
                if isinstance(v, dict):
                    return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
                elif isinstance(v, tuple):
                    return list(v)
                else:
                    return v

            def ds2yml(ds: xr.Dataset) -> dict:
                """
                Converts the input xr.Dataset to a format compatible with yaml.load.

                Args:
                    ds (xr.Dataset): NetCDF data loaded as a xr.Dataset
                """
                d = ds.to_dict()
                return fmt({**{k: v['data'] for k, v in d['coords'].items()},
                            **d['data_vars']})
            return ds2yml(xr.open_dataset(filename))
        else:
            raise ValueError(f"Unsupported file extension: {ext}")
XrResourceLoader.add_constructor('!include', XrResourceLoader.include)

# Add regex matching for scientific notation
XrResourceLoader.add_implicit_resolver(
    u'tag:yaml.org,2002:float',
    re.compile(u'''^(?:
     [-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+]?[0-9]+)?
    |[-+]?(?:[0-9][0-9_]*)(?:[eE][-+]?[0-9]+)
    |\\.[0-9_]+(?:[eE][-+][0-9]+)?
    |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*
    |[-+]?\\.(?:inf|Inf|INF)
    |\\.(?:nan|NaN|NAN))$''', re.X),
    list(u'-+0123456789.'))

def load_yaml(filename: str, loader=XrResourceLoader) -> dict:
    """
    Opens ``filename`` and loads the content into a dictionary with the ``yaml.load``
    function from pyyaml.

    Args:
        filename (str): Path to the local file to be loaded.
        loader (yaml.SafeLoader, optional): Defaults to XrResourceLoader.

    Returns:
        dict: Dictionary representation of the YAML file given in ``filename``.
    """
    with open(filename) as fid:
        return yaml.load(fid, loader)

def _add_local_schemas_to(resolver, schema_folder, base_uri, schema_ext_lst=['.json', '.yaml', '.yml']):
    '''Function from https://gist.github.com/mrtj/d59812a981da17fbaa67b7de98ac3d4b#file-local_ref-py
    Add local schema instances to a resolver schema cache.

    Args:
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

def validate(input: dict | str | Path, schema_type: str) -> None:
    """
    Validates a given windIO input based on the selected schema type.

    Args:
        input (dict | str | Path): Input data or path to file to be validated.
        schema_type (str): Type of schema to be used for validation. This must map to one
            of the schema files available in the ``schemas/plant`` or ``schemas/turbine`` folders.
            Examples of valid schema types are 'plant/wind_energy_system' or
            '`turbine/IEAontology_schema`'.

    Raises:
        FileNotFoundError: If the schema type is not found in the schemas folder.
        TypeError: If the input type is not supported.
        jsonschema.exceptions.ValidationError: If the input data fails validation
            against the schema.
        jsonschema.exceptions.SchemaError: if the schema itself is invalid.
    
    Returns:
        None
    """
    schema_file = Path(windIO.schemas.__file__).parent / f"{schema_type}.yaml"
    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file {schema_file} not found.")

    if type(input) is dict:
        data = copy.deepcopy(input)
    elif type(input) in [str, Path, PosixPath, WindowsPath]:
        data = load_yaml(input)
    else:
        raise TypeError(f"Input type {type(input)} is not supported.")

    schema = load_yaml(schema_file)
    base_uri = 'https://www.example.com/schemas/'
    resolver = jsonschema.RefResolver(base_uri=base_uri, referrer=schema)
    schema_folder = Path(schema_file).parent
    _add_local_schemas_to(resolver, schema_folder, base_uri)
    jsonschema.validate(data, schema, resolver=resolver)
