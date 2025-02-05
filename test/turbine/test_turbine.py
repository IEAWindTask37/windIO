import unittest
import yaml
from pathlib import Path
import windIO

import yaml
from jsonschema import Draft7Validator


class TestRegression(unittest.TestCase):
    def test_IEA_15_240_RWT(self):
        path2yaml = Path(__file__).parent / "IEA-15-240-RWT.yaml"

        # Validate the file
        windIO.validate(path2yaml, "turbine/IEAontology_schema")

        # Verify the file loads
        windIO.load_yaml(path2yaml)

    def test_IEA_15_240_RWT_VolturnUS_S(self):
        path2yaml = Path(__file__).parent / "IEA-15-240-RWT_VolturnUS-S.yaml"

        # Validate the file
        windIO.validate(path2yaml, "turbine/IEAontology_schema")

        # Verify the file loads
        windIO.load_yaml(path2yaml)
    
    def test_valid_schema(self):
        schema = yaml.load(
            open(Path(windIO.schemas.turbine.__file__).parent / "IEAontology_schema.yaml", "r"),
            Loader=yaml.FullLoader
        )

        Draft7Validator.META_SCHEMA["additionalProperties"] = False
        Draft7Validator.META_SCHEMA["properties"]["definitions"]["additionalProperties"] = True
        Draft7Validator.META_SCHEMA["properties"]["units"] = dict(type="string")
        Draft7Validator.META_SCHEMA["properties"]["optional"] = Draft7Validator.META_SCHEMA["properties"]["required"]

        Draft7Validator.check_schema(schema)

        def recursive_require_optional_in_properties(schema, name_list=None):
            if name_list is None:
                name_list = []
            for name in schema.get("required", []):
                assert name in schema["properties"], f"Required property: '{name}' is not in `properties` for {name_list}"
            for name in schema.get("optional", []):
                assert name in schema["properties"], f"Optional property: '{name}' is not in `properties` for {name_list}"
            for name, val in schema.items():
                if name in ["if", "then", "else"]:
                    continue
                if isinstance(val, dict):
                    recursive_require_optional_in_properties(val, name_list+[name])
                if isinstance(val, list):
                    for iel, el in enumerate(val):
                        if isinstance(el, dict):
                            recursive_require_optional_in_properties(el, name_list+[name, iel])
                            
        recursive_require_optional_in_properties(schema)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegression))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
