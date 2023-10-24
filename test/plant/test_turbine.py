from windIO.utils.pywake_utils import yml2WindTurbines
from windIO.utils import plant_examples_data_path
from py_wake.examples.data.iea37._iea37 import IEA37_WindTurbines
import numpy.testing as npt
import numpy as np


def test_3_350_turbine():
    ref = IEA37_WindTurbines()
    wt = yml2WindTurbines(plant_examples_data_path + "plant_energy_turbine/IEA37_3.35MW_turbine.yaml")

    npt.assert_equal(wt.diameter(), ref.diameter())
    npt.assert_equal(wt.hub_height(), ref.hub_height())
    u = np.linspace(0, 30, 100)
    npt.assert_array_almost_equal(wt.power(u), ref.power(u))
    u = np.linspace(4, 25, 100)
    npt.assert_array_almost_equal(wt.ct(u), ref.ct(u))
