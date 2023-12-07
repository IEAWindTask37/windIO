import numpy as np
import xarray as xr
from windIO.utils.yml_utils import load_yaml, XrResourceLoader
from py_wake.wind_turbines import WindTurbine
from py_wake.wind_turbines.power_ct_functions import CubePowerSimpleCt, PowerCtFunctions
from py_wake.site.xrsite import XRSite
from py_wake.deficit_models.gaussian import IEA37SimpleBastankhahGaussian
import matplotlib.pyplot as plt
from test.plant import examples_data_path


def yml2Site(yml, interp_method='nearest'):
    resource = load_yaml(yml, XrResourceLoader)
    if 'energy_resource' in resource:
        resource = resource['energy_resource']
    data = resource['wind_resource']
    ds = xr.Dataset({k: (v['dims'], v['data']) for k, v in data.items() if hasattr(v, 'keys') and 'dims' in v},
                    coords={k: v for k, v in data.items() if not hasattr(v, 'keys')})
    return xr2Site(ds)


def xr2Site(ds, interp_method='nearest'):
    ds = ds.rename(**{k: v for k, v in [('height', 'h'),
                                        ('wind_direction', 'wd'),
                                        ('wind_speed', 'ws'),
                                        ('wind_turbine', 'i'),
                                        ('probability', 'P'),
                                        ('weibull_a', 'Weibull_A'),
                                        ('weibull_k', 'Weibull_k'),
                                        ('sector_probability', 'Sector_frequency'),
                                        ('turbulence_intensity', 'TI')] if k in ds})
    if 'ws' in ds:
        return XRSite(ds, default_ws=ds.ws, interp_method=interp_method)
    else:
        return XRSite(ds, interp_method=interp_method)


def yml2WindTurbines(yml):
    wt = load_yaml(yml)
    power = wt['performance']

    if 'power_curve' in power:
        raise NotImplementedError()
    elif 'cp_curve' in power:
        raise NotImplementedError()
    else:
        ws_cutin = power['cutin_wind_speed']
        ws_cutout = power['cutout_wind_speed']
        ws_rated = power['rated_wind_speed']
        power_rated = power['rated_power']

        def power_func(ws):
            ws = np.asarray(ws)

            return np.where((ws > ws_cutin) & (ws <= ws_cutout),
                            np.minimum(power_rated * ((ws - ws_cutin) / (ws_rated - ws_cutin))**3,
                                       power_rated),
                            0)

        def ct_func(ws):
            return np.interp(ws,
                             power['Ct_curve']['Ct_wind_speeds'],
                             power['Ct_curve']['Ct_values'])

    return WindTurbine(name=wt['name'], diameter=wt['rotor_diameter'], hub_height=wt['hub_height'],
                       powerCtFunction=PowerCtFunctions(power_func, 'w', ct_func))


def ymlSystem2PyWake(wind_energy_system_yml, windFarmModel):
    wes = load_yaml(wind_energy_system_yml)
    wf = wes['wind_farm']
    x, y = [wf['layouts']['initial_layout']['coordinates'][xy] for xy in 'xy']

    wt = yml2WindTurbines(wf['turbines'])
    site = yml2Site(wes['site'])
    return windFarmModel(site=site, windTurbines=wt), (x, y)


if __name__ == '__main__':
    wfm, (x, y) = ymlSystem2PyWake(examples_data_path + 'wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml',
                                   IEA37SimpleBastankhahGaussian)
    ref = np.array([9444.60012, 8497.90004, 11383.32869, 14173.40367,
                    20979.36776, 25590.86774, 39252.85757, 43197.65856,
                    23800.39229, 13539.36766, 15022.89800, 32644.44314,
                    71157.32322, 18092.10102, 12326.48041, 7838.58128])

    sim_res = wfm(x, y, wd=np.arange(0, 360, 22.5))
    print("AEP", sim_res.aep(normalize_probabilities=True).sum())
    sim_res.flow_map(wd=270).plot_wake_map()
    plt.show()
