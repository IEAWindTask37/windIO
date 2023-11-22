Environment
------------

The field :code:`environment` includes the data characterizing air and water.

.. literalinclude:: ../../test/turbine/IEA-15-240-RWT.yaml
    :start-after: environment
    :end-before: bos

:code:`air_density` : Float, kg/m3
    Density of air. 
:code:`air_dyn_viscosity` : Float, kg/(m*s)
    Dynamic viscosity of air.
:code:`weib_shape_parameter` : Float 
    Shape parameter of the Weibull wind distribution. 
:code:`air_speed_sound` : Float, m/s
    Speed of sound in air. 
:code:`shear_exp` : Float 
    Shear exponent of the wind.
:code:`water_density` : Float, kg/m3
    Density of water. 
:code:`water_dyn_viscosity` : Float, kg/(m*s)
    Dynamic viscosity of air. 
:code:`soil_shear_modulus` : Float, Pa
    Shear modulus of the soil. 
:code:`soil_poisson` : Float
    Poisson ratio of the soil. 
:code:`water_depth` : Float, m
    Depth of the water at the site
:code:`significant_wave_height` : Float, m
    Significant wave height at the site
:code:`significant_wave_period` : Float, m
    Significant wave period at the site