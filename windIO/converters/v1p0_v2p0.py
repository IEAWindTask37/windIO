import os
from copy import deepcopy
from windIO.utils.yml_utils import load_yaml, write_yaml

class v0p1_to_v1p0:
    def __init__(self, filename_v1p0, filename_v2p0, **kwargs) -> None:
        self.filename_v1p0 = filename_v1p0
        self.filename_v2p0 = filename_v2p0

    def convert(self):
        # Read the input yaml
        dict_v1p0 = load_yaml(self.filename_v1p0)
        
        # Copy the input windio dict
        dict_v2p0 = deepcopy(dict_v1p0)

        write_yaml(dict_v2p0, self.filename_v2p0)


if __name__ == "__main__":
    
    filename_v1p0 = os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        "v1p0",
                        "IEA-15-240-RWT.yaml"
                    )
    
    filename_v2p0 = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "v2p0",
                    "IEA-15-240-RWT.yaml"
                )
    
    converter = v0p1_to_v1p0(filename_v1p0, filename_v2p0)
    converter.convert()