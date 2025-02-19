from windIO.utils.yml_utils import validate_yaml, load_yaml

def check_15_MW():
    turbine_data = load_yaml('../../examples/plant/plant_energy_turbine/IEA37_15MW_turbine.yaml')
    assert(turbine_data['rotor_diameter'] == 240)
