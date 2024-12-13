import numpy as np
import numpy.testing as npt
import pytest
from windIO.utils.yml_utils import validate
from windIO.utils import plant_examples_data_path, plant_schemas_path


def test_timeseries():
    assert validate(
        plant_examples_data_path + "plant_energy_resource/timeseries.yaml",
        plant_schemas_path + "energy_resource.yaml"
    ) is None

def test_timeseries_netcdf():
    assert validate(
        plant_examples_data_path + "plant_energy_resource/timeseries_with_netcdf.yaml",
        plant_schemas_path + "energy_resource.yaml"
    ) is None

def test_timeseries_vertical_variation():
    assert validate(
        plant_examples_data_path + "plant_energy_resource/timeseries_vertical_variation.yaml",
        plant_schemas_path + "energy_resource.yaml"
    ) is None
