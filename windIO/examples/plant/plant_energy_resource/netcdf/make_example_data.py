import xarray as xr
import numpy as np
import yaml
from pathlib import Path
import matplotlib.pyplot as plt
from py_wake.examples.data.ParqueFicticio._parque_ficticio import ParqueFicticioSite


def xr2yml(name, ds, filename):
    def fmt(v):
        if isinstance(v, dict):
            return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
        elif isinstance(v, tuple):
            return list(v)
        else:
            return v
    data_dict = fmt(ds.to_dict())

    # yaml with all
    yml = yaml.dump({'name': name, 'wind_resource': {**{k: v['data'] for k, v in data_dict['coords'].items()},
                                                     **data_dict['data_vars']}})
    Path(filename).write_text(yml)

    # yaml with data in netcdf
    ds.to_netcdf(filename.replace(".yaml", '.nc'))
    yml_nc = yaml.dump({'name': name, 'wind_resource': "!include %s" % filename.replace('yaml', 'nc')}).replace("'", "")
    Path(filename.replace(".yaml", '_nc.yaml')).write_text(yml_nc)
    return yml


if __name__ == '__main__':

    # ===================================================================================================================
    # Uniform Resource
    # ===================================================================================================================
    # uniform site (https://github.com/byuflowlab/iea37-wflo-casestudies/blob/master/cs1-2/iea37-windrose.yaml)
    f = [.025, .024, .029, .036, .063, .065, .100, .122, .063, .038, .039, .083, .213, .046, .032, .022]
    WS = 9.8
    ds = xr.Dataset(
        data_vars={'probability': ('wind_direction', f), 'turbulence_intensity': 0.075},
        coords={'wind_direction': np.linspace(0, 360, len(f), endpoint=False),
                'wind_speed': WS, })
    xr2yml("IEA Wind Task 37 Plant Energy Resource", ds, "UniformResource.yaml")

    # ===================================================================================================================
    # Uniform Weibull Resource
    # ===================================================================================================================

    f = np.array([3.597152, 3.948682, 5.167395, 7.000154, 8.364547, 6.43485,
                  8.643194, 11.77051, 15.15757, 14.73792, 10.01205, 5.165975]) / 100
    A = [9.176929, 9.782334, 9.531809, 9.909545, 10.04269, 9.593921,
         9.584007, 10.51499, 11.39895, 11.68746, 11.63732, 10.08803]
    k = [2.392578, 2.447266, 2.412109, 2.591797, 2.755859, 2.595703,
         2.583984, 2.548828, 2.470703, 2.607422, 2.626953, 2.326172]
    ds = xr.Dataset(
        data_vars={'sector_probability': ('wind_direction', f),
                   'weibull_a': ('wind_direction', A), 'weibull_k': ('wind_direction', k),
                   'turbulence_intensity': 0.075},
        coords={'wind_direction': np.linspace(0, 360, len(f), endpoint=False)})
    xr2yml('Hornsrev1 Energy Resource', ds, "UniformWeibullResource.yaml")

    # NonGridded site. 16 WT with speedup = 1+.01*wt_index
    site = ParqueFicticioSite()
    x, y = site.initial_position.T
    lw = site.local_wind(x_i=x, y_i=y, h_i=70, wd=np.arange(0, 60, 30), ws=[8, 10])
    ds = xr.Dataset(
        data_vars={'sector_probability': (('wind_turbine', 'wind_direction'), lw.Sector_frequency.values),
                   'weibull_a': (('wind_turbine', 'wind_direction'), lw.Weibull_A.values),
                   'weibull_k': (('wind_turbine', 'wind_direction'), lw.Weibull_k.values),
                   'turbulence_intensity': (('wind_turbine', 'wind_direction', 'wind_speed'), lw.TI.values),
                   'x': ('wind_turbine', lw.x),
                   'y': ('wind_turbine', lw.y),
                   'height': ('wind_turbine', lw.h),
                   },
        coords={'wind_direction': lw.wd.values, 'wind_speed': lw.ws.values, 'wind_turbine': lw.i.values})

    xr2yml('Parque Ficticio Energy Resource', ds, "WTResource.yaml")

    # ===================================================================================================================
    # Gridded Resource
    # ===================================================================================================================

    src = ParqueFicticioSite().ds.sel(ws=[8, 10], wd=[0, 30])
    ds = xr.Dataset(
        data_vars={'sector_probability': (('x', 'y', 'height', 'wind_direction'), src.Sector_frequency.values),
                   'weibull_a': (('x', 'y', 'height', 'wind_direction'), src.Weibull_A.values),
                   'weibull_k': (('x', 'y', 'height', 'wind_direction'), src.Weibull_k.values),

                   },
        coords={'wind_direction': lw.wd.values, 'wind_speed': lw.ws.values,
                'x': src.x.values, 'y': src.y.values, 'height': src.h.values})

    xr2yml('Parque Ficticio Energy Resource', ds, "GriddedResource.yaml")


#     ParqueFicticioSite().ds
#     f = [.025, .024, .029, .036, .063, .065, .100, .122, .063, .038, .039, .083, .213, .046, .032, .022]
#     x = y = np.arange(-2000, 2500, 500)
#     X, Y = np.meshgrid(x, y)
#
#     ds = xr.Dataset(
#         data_vars={'Speedup': (['x', 'y'], 1 + 0.1 * x / x.max() + 0.1 * np.cos(Y / y.max())), 'P': ('wd', f)},
#         coords={'wd': np.linspace(0, 360, len(f), endpoint=False),
#                 'x': x,
#                 'y': y})
#     ds.Speedup.plot(x='x')
#     plt.show()
#     ds.to_netcdf("GriddedSite.nc")
#     xr2yml(ds, "GriddedSite.yml")
