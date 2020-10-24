import unittest
import os
from jsonschema import validate
try:
    import ruamel_yaml as yaml
    loader = ry.Loader
except:
    try:
        import ruamel.yaml as yaml
        loader = ry.Loader
    except:
        import yaml
        loader = yaml.FullLoader
        print('No module named ruamel.yaml or ruamel_yaml, so using substitute')

path2schema = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) + os.sep + 'windIO' + os.sep + 'turbine' + os.sep + "IEAontology_schema.yaml"

def load_yaml(fname_input):
    with open(fname_input, 'r') as f:
        input_yaml = yaml.load(f, Loader=loader)
    return input_yaml


class TestRegression(unittest.TestCase):
    
    def test_IEA_3_4_130_RWT(self):
        
        path2yaml = os.path.dirname( os.path.realpath(__file__) ) + os.sep + "turbine_example.yaml"
        # Read the input yaml
        with open(path2yaml, 'r') as myfile:
            inputs = myfile.read()

        # Read the schema
        with open(path2schema, 'r') as myfile:
            schema = myfile.read()

        # Run the validate class from the jsonschema library
        validate(load_yaml(inputs), load_yaml(schema))

        # Move it to a dictionary called wt_data
        wt_data = load_yaml(inputs)

        return None 


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegression))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
    
    
