
from windIO.utils.pywake_utils import yml2Site, xr2Site
import numpy.testing as npt
import numpy as np
import pytest
from py_wake import IEA37SimpleBastankhahGaussian, NOJ
from py_wake.examples.data.iea37._iea37 import IEA37_WindTurbines, IEA37Site
import xarray as xr
from py_wake.examples.data.hornsrev1 import V80, Hornsrev1Site
from py_wake.examples.data.ParqueFicticio._parque_ficticio import ParqueFicticioSite
from test.plant import examples_data_path


@pytest.mark.parametrize('ext', ['.yaml', '_nc.yaml', '.nc'])
def test_uniform_resource(ext):
    filename = "UniformResource" + ext
    if ext.endswith('.yaml'):
        site = yml2Site(examples_data_path + "/plant_energy_resource/" + filename)
    else:
        site = xr2Site(xr.open_dataset(examples_data_path + "/plant_energy_resource/" + filename))

    wd = np.arange(0, 360, 22.5)
    npt.assert_array_equal(site.ds.P.sel(wd=wd), [0.025, 0.024, 0.029, 0.036, 0.063, 0.065, 0.1,
                                                  0.122, 0.063, 0.038, 0.039, 0.083, 0.213, 0.046, 0.032, 0.022])
    npt.assert_array_equal(site.ds.ws, [9.8])
    npt.assert_array_equal(site.ds.TI, [0.075])
    wts = IEA37_WindTurbines()
    ref_site = IEA37Site(16)
    x, y = ref_site.initial_position.T

    npt.assert_array_equal(IEA37SimpleBastankhahGaussian(ref_site, wts)(x, y).aep(),
                           IEA37SimpleBastankhahGaussian(site, wts)(x, y).aep(), )


@pytest.mark.parametrize('ext', ['.yaml', '_nc.yaml', '.nc'])
def test_uniform_weibull_resource(ext):
    filename = "UniformWeibullResource" + ext
    if ext.endswith('.yaml'):
        site = yml2Site(examples_data_path + "/plant_energy_resource/" + filename)
    else:
        site = xr2Site(xr.open_dataset(examples_data_path + "/plant_energy_resource/" + filename))

    wd = np.arange(0, 360, 30)

    f = [3.597152, 3.948682, 5.167395, 7.000154, 8.364547, 6.43485,
         8.643194, 11.77051, 15.15757, 14.73792, 10.01205, 5.165975]
    A = [9.176929, 9.782334, 9.531809, 9.909545, 10.04269, 9.593921,
         9.584007, 10.51499, 11.39895, 11.68746, 11.63732, 10.08803]
    k = [2.392578, 2.447266, 2.412109, 2.591797, 2.755859, 2.595703,
         2.583984, 2.548828, 2.470703, 2.607422, 2.626953, 2.326172]

    npt.assert_array_equal(site.ds.Weibull_A.sel(wd=wd), A)
    npt.assert_array_equal(site.ds.Weibull_k.sel(wd=wd), k)
    npt.assert_array_almost_equal(site.ds.Sector_frequency.sel(wd=wd) * 100, f)
    npt.assert_array_equal(site.ds.TI, [0.075])

    wts = V80()
    ref_site = Hornsrev1Site()
    x, y = ref_site.initial_position.T
    npt.assert_array_almost_equal(NOJ(ref_site, wts)(x, y).aep(),
                                  NOJ(site, wts)(x, y).aep(), )


@pytest.mark.parametrize('ext', ['.yaml', '_nc.yaml', '.nc'])
def test_wt_resource(ext):
    filename = "GriddedResource" + ext
    if ext.endswith('.yaml'):
        site = yml2Site(examples_data_path + "/plant_energy_resource/" + filename)
    else:
        site = xr2Site(xr.open_dataset(examples_data_path + "/plant_energy_resource/" + filename))
    site.ds['TI'] = .075

    ref_site = ParqueFicticioSite()

    npt.assert_array_equal(ref_site.ds.Weibull_A.interp(x=263828, y=6505664, wd=15),
                           site.ds.Weibull_A.interp(x=263828, y=6505664, wd=15))
    npt.assert_array_equal(ref_site.ds.Weibull_k.interp(x=263828, y=6505664, wd=15),
                           site.ds.Weibull_k.interp(x=263828, y=6505664, wd=15))
    npt.assert_array_equal(ref_site.ds.Sector_frequency.interp(x=263828, y=6505664, wd=15),
                           site.ds.Sector_frequency.interp(x=263828, y=6505664, wd=15))
