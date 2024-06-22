from windIO.utils.pywake_utils import ymlSystem2PyWake
from windIO.utils.yml_utils import load_yaml
from py_wake.deficit_models.gaussian import IEA37SimpleBastankhahGaussian
from topfarm._topfarm import TopFarmProblem
from topfarm.constraint_components.boundary import CircleBoundaryConstraint
from topfarm.cost_models.py_wake_wrapper import PyWakeAEPCostModelComponent
from topfarm.plotting import XYPlotComp


def ymlSystem2TopFarm(wind_energy_system_yml, **kwargs):
    wes = load_yaml(wind_energy_system_yml)
    wfm, (x, y) = ymlSystem2PyWake(wes, IEA37SimpleBastankhahGaussian)
    constraints = []
    boundary = wes['site']['boundaries']
    for k, v in boundary.items():
        if k == 'circle':
            center = [v['center'][xy] for xy in 'xy']
            radius = v['radius']
            constraints.append(CircleBoundaryConstraint(center, radius))
        else:
            raise NotImplementedError()

    tf_kwargs = {'design_vars': {'x': x, 'y': y},
                 'cost_comp': PyWakeAEPCostModelComponent(windFarmModel=wfm, n_wt=len(x)),
                 'constraints': [CircleBoundaryConstraint(center, radius)],
                 'plot_comp': XYPlotComp()}
    tf_kwargs.update(kwargs)
    return TopFarmProblem(**tf_kwargs)
