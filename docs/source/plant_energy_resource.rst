.. _energy_resource:

Energy Resource
===============

The :code:`energy_resource` contains information for the wind resource associated with the wind energy system.
Required are a :code:`name` for the energy resource, and a :code:`wind_resource` definition, detailed
:ref:`below <wind_resource_properties>`.

.. _plant_energy_resource_properties:

Properties
----------

:code:`name` : String
    Unique identifier of the wind energy resource.

:code:`wind_resource` : Object
    Nested dictionary structure of the relevant wind energy resource information for the site.
    Requires either the :code:`probability` definition or a :code:`weibull_a`, :code:`weibull_k`,
    :code:`sector_probability` group definition.

.. _wind_resource_properties:

wind_resource Properties
````````````````````````

The plant schema supports many options to define a wind energy resource. Currently required
properties include either a :code:`probability` or a set of :code:`weibull_a`, :code:`weibull_k`,
and :code:`sector_probability`, all of which can depend on wind speed, wind direction, and/or position.
These requirements are meant to be a bare minimum amount of information required, and severall additional
characteristics are supported by the schema. As wind resource data can become quite large, the schema also
supports using NetCDF files to contain the large data structures. These requirements and the additional
options are detailed below, followed by several example :code:`energy_resource` definitions. More examples
can be found `here <https://github.com/IEAWindSystems/windIO/tree/master/examples/plant/plant_energy_resource>`_.

:code:`wind_direction` : Array or Number
    Either an array of numbers or a single number representing the wind direction(s).

:code:`wind_speed` : Array or Number
    Either an array of numbers or a single number representing the wind speed(s).

:code:`wind_turbine` : Array or Number
    Either an array of numbers or a single number representing a specific wind turbine ID.

:code:`x` : Array or Number
    Either an array of numbers or a single number representing the x-coordinate(s) at which wind
    data are defined. The array of numbers can be multi-dimensional, associated with its dependencies.

:code:`y` : Array or Number
    Either an array of numbers or a single number representing the y-coordinate(s) at which wind
    data are defined. The array of numbers can be multi-dimensional, associated with its dependencies.

:code:`height` : Array or Number
    Either an array of numbers or a single number representing the z-coordinate(s) at which wind
    data are defined. The array of numbers can be multi-dimensional, associated with its dependencies.

.. _probability:

:code:`probability` : Array
    Either a mulit-dimensional array of numbers or a single array of numbers containing the probability
    for each associated wind condition.

:code:`weibull_a` : Array
    Either a mulit-dimensional array of numbers or a single array of numbers containing the Weibull scale
    for each associated wind condition.

:code:`weibull_k` : Array
    Either a mulit-dimensional array of numbers or a single array of numbers containing the Weibull shape
    for each associated wind condition.

:code:`sector_probability` : Array
    Either a mulit-dimensional array of numbers or a single array of numbers containing the probability of
    wind directions.

:code:`turbulence_intensity` : Array
    Either a mulit-dimensional array of numbers or a single array of numbers containing the turbulence 
    intensity for each associated wind condition.

:code:`shear` : Object
    Nested dictionary object containing information on wind shear. Requires a shear reference height, 
    :code:`h_ref`, and a shear exponent, :code:`alpha`.

.. _plant_energy_resource_examples:

Examples
--------

Uniform Resource
````````````````

In this example, wind directions and associated probabilities are specified, along with a single
wind speed and turbulence intensity.

.. literalinclude:: ../../windIO/examples/plant/plant_energy_resource/UniformResource.yaml
    :start-at: name:
    :end-at: wind_speed:

Uniform Weibull Resource
````````````````````````

In this example, wind directions and associated probabilities are specified, along with Weibull parameters
for each wind direction. 

.. literalinclude:: ../../windIO/examples/plant/plant_energy_resource/UniformWeibullResource.yaml
    :start-at: name:
    :end-at: - 330.0

IEA Wind Task 37 Case Study 3 Plant Energy Resource
```````````````````````````````````````````````````

In this example, wind directions and associated probabilities are specified, along with Weibull parameters
for each wind direction. 

.. literalinclude:: ../../windIO/examples/plant/plant_energy_resource/IEA37_case_study_3_energy_resource.yaml
    :start-at: name:
    :end-at: dims:
