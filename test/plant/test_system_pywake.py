from windIO.utils import plant_examples_data_path
from windIO.utils.yml_utils import load_yaml
from windIO.utils.pywake_utils import ymlSystem2PyWake
from py_wake.deficit_models.gaussian import IEA37SimpleBastankhahGaussian
import numpy as np
import numpy.testing as npt
import pytest


try:
    import topfarm
    from topfarm._topfarm import TopFarmProblem
    from topfarm.cost_models.py_wake_wrapper import PyWakeAEPCostModelComponent
    from topfarm.constraint_components.boundary import CircleBoundaryConstraint
    from topfarm.plotting import XYPlotComp
    from windIO.utils.topfarm_utils import ymlSystem2TopFarm
    from test.plant import examples_data_path
except ModuleNotFoundError:
    topfarm = None

    def test_IEA37_case_study1_16wt_PyWake():
        if topfarm is None:
            pytest.xfail()
        wfm, (x, y) = ymlSystem2PyWake(examples_data_path + 'wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml',
                                       IEA37SimpleBastankhahGaussian)
        ref = np.array([9444.60012, 8497.90004, 11383.32869, 14173.40367,
                        20979.36776, 25590.86774, 39252.85757, 43197.65856,
                        23800.39229, 13539.36766, 15022.89800, 32644.44314,
                        71157.32322, 18092.10102, 12326.48041, 7838.58128])

        sim_res = wfm(x, y, wd=np.arange(0, 360, 22.5))
        aep = sim_res.aep(normalize_probabilities=True)
        npt.assert_array_almost_equal(aep.sum(['wt', 'ws']) * 1e3, ref, 5)

    def test_IEA37_case_study1_16wt_TopFarm2():
        if topfarm is None:
            pytest.xfail()
        tf = ymlSystem2TopFarm(examples_data_path + 'wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml')
        wfm = tf.cost_comp.windFarmModel
        wfm.verbose = False
        wfm.site.default_wd = np.arange(0, 360, 22.5)
        cost = tf.evaluate()[0]
        npt.assert_almost_equal(-cost * 1e3, 366941.57116, 4)
        # tf.plot_comp.show()
