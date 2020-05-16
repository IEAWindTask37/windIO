Environment
------------

The field :code:`environment` includes the data characterizing air and water.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Environment
    :end-before: # Costs

The entries are:
   -  :code:`air_density`: Float of the density of air, expressed in kg/m3. 
   -  :code:`air_dyn_viscosity`: Float of the dynamic viscosity of air, expressed in kg/(m*s). 
   -  :code:`weib_shape_parameter`: Float of the shape parameter of the Weibull wind distribution. 
   -  :code:`air_speed_sound`: Float of the speed of sound in air, expressed in m/s. 
   -  :code:`shear_exp`: Float of the shear exponent of the wind.
   -  :code:`water_density`: Float of the density of water, expressed in kg/m3. 
   -  :code:`water_dyn_viscosity`: Float of the dynamic viscosity of air, expressed in kg/(m*s). 
   -  :code:`soil_shear_modulus`: Float of the shear modulus of the soil, expressed in Pa. 
   -  :code:`soil_poisson`: Float of the Poisson ratio of the soil. 