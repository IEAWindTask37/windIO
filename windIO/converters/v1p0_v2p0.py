import os
from copy import deepcopy
from windIO.utils.yml_utils import load_yaml, write_yaml
import numpy as np

class v1p0_to_v2p0:
    def __init__(self, filename_v1p0, filename_v2p0, **kwargs) -> None:
        self.filename_v1p0 = filename_v1p0
        self.filename_v2p0 = filename_v2p0

    def convert(self):
        # Read the input yaml
        dict_v1p0 = load_yaml(self.filename_v1p0)
        
        # Copy the input windio dict
        dict_v2p0 = deepcopy(dict_v1p0)

        # Add windIO version
        dict_v2p0["windIO_version"] = "2.0"
        
        # Switch from pitch_axis to section_offset_x
        # First interpolate on chord grid
        blade_bem = dict_v1p0["components"]["blade"]["outer_shape_bem"]
        pitch_axis_grid =  blade_bem["pitch_axis"]["grid"]
        pitch_axis_values =  blade_bem["pitch_axis"]["values"]
        chord_grid =  blade_bem["chord"]["grid"]
        chord_values =  blade_bem["chord"]["values"]
        section_offset_x_grid = chord_grid
        pitch_axis_interp = np.interp(section_offset_x_grid,
                                      pitch_axis_grid,
                                      pitch_axis_values,
                                      )
        # Now dimensionalize offset using chord
        section_offset_x_values = pitch_axis_interp * chord_values
        dict_v2p0["components"]["blade"]["outer_shape_bem"].pop("pitch_axis")
        dict_v2p0["components"]["blade"]["outer_shape_bem"]["section_offset_x"] = {}
        dict_v2p0["components"]["blade"]["outer_shape_bem"]["section_offset_x"]["grid"] = section_offset_x_grid
        dict_v2p0["components"]["blade"]["outer_shape_bem"]["section_offset_x"]["values"] = section_offset_x_values
        
        # Convert twist from rad to deg
        twist_rad = dict_v2p0["components"]["blade"]["outer_shape_bem"]["twist"]["values"]
        dict_v2p0["components"]["blade"]["outer_shape_bem"]["twist"]["values"] = np.rad2deg(twist_rad)

        # Convert field `rotation` from rad to deg when defined in webs/layers
        blade_struct = dict_v2p0["components"]["blade"]["internal_structure_2d_fem"]
        for iweb in range(len(blade_struct['webs'])):
            if "rotation" in blade_struct["webs"][iweb]:
                rotation_rad = blade_struct["webs"][iweb]["rotation"]["values"]
                blade_struct["webs"][iweb]["rotation"]["values"] = np.rad2deg(rotation_rad)
        for ilayer in range(len(blade_struct['layers'])):
            if "rotation" in blade_struct["layers"][ilayer]:
                rotation_rad = blade_struct["layers"][ilayer]["rotation"]["values"]
                blade_struct["layers"][ilayer]["rotation"]["values"] = np.rad2deg(rotation_rad)
        
        

        # Print out
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
    
    converter = v1p0_to_v2p0(filename_v1p0, filename_v2p0)
    converter.convert()