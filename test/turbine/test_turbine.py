import os
import unittest

import yaml
from jsonschema import Draft7Validator, validate

path2schema = (
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    + os.sep
    + "windIO"
    + os.sep
    + "turbine"
    + os.sep
    + "IEAontology_schema.yaml"
)


class TestRegression(unittest.TestCase):
    def test_IEA_15_240_RWT(self):
        path2yaml = (
            os.path.dirname(os.path.realpath(__file__))
            + os.sep
            + "IEA-15-240-RWT.yaml"
        )
        # Read the input yaml
        with open(path2yaml, "r") as myfile:
            inputs = myfile.read()

        # Read the schema
        with open(path2schema, "r") as myfile:
            schema = myfile.read()

        # Run the validate class from the jsonschema library
        validate(
            yaml.load(inputs, Loader=yaml.FullLoader),
            yaml.load(schema, Loader=yaml.FullLoader),
        )

        # Move it to a dictionary
        _ = yaml.load(inputs, Loader=yaml.FullLoader)

        return None

    def test_IEA_15_240_RWT_VolturnUS_S(self):
        path2yaml = (
            os.path.dirname(os.path.realpath(__file__))
            + os.sep
            + "IEA-15-240-RWT.yaml"
        )
        # Read the input yaml
        with open(path2yaml, "r") as myfile:
            inputs = myfile.read()

        # Read the schema
        with open(path2schema, "r") as myfile:
            schema = myfile.read()

        # Run the validate class from the jsonschema library
        validate(
            yaml.load(inputs, Loader=yaml.FullLoader),
            yaml.load(schema, Loader=yaml.FullLoader),
        )

        # Move it to a dictionary
        _ = yaml.load(inputs, Loader=yaml.FullLoader)

        return None
    
    def test_valid_schema(self):
        with open(path2schema, "r") as file:
            schema = yaml.load(file, Loader=yaml.FullLoader)
        
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