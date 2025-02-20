Wind Farm
*********

The wind farm schema deals with parameters of the wind farm. Required are a :code:`layouts` definition
and a :code:`turbines` definition. Additional properties can be included as needed, but don't currently
have associated schemas.

.. literalinclude:: ../../windIO/examples/plant/plant_wind_farm/IEA37_case_study_3_wind_farm.yaml
    :start-at: name:
    :end-at: turbines:

.. _wind_farm_properties:

Properties
==========

:code:`layouts` : Object
    An object that has a required property :code:`coordinates`, which is an object that consists of two
    arrays, :code:`x` and :code:`y`, which contain the x- and y-coordinates for the turbines.

:code:`turbines` : Object
    An object containing a nested dictionary with various turbine-defining parameters. For specfic properties,
    see :ref:`below <turbine_properties>`.

.. _turbine_properties:

turbine Properties
------------------

:code:`name` : String
    Unique identifier of the turbine.

:code:`hub_height` : Number
    A number specifying the hub height of the turbine in meters.
    
:code:`rotor_diameter` : Number
    A number specifying the rotor diameter of the turbine in meters.

:code:`TSR` : Number
    A number specifying the tip-speed ratio of the turbine.

:code:`performance` : Object
    An object containing a nested dictionary of turbine performance characteristics. Required combinations of
    properties include:

    #. :code:`Cp_curve` and :code:`Ct_curve`
    #. :code:`power_curve` and :code:`Ct_curve`
    #. :code:`rated_power`, :code:`rated_wind_speed`, :code:`cutin_wind_speed`, :code:`cutout_wind_speed`, and :code:`Ct_curve`.
    
    For specific properties, see :ref:`below <performance_properties>`.

.. _performance_properties:

performance Properties
----------------------

:code:`Cp_curve` : Object
    An object containing a nested dictionary of Cp performance characteristics. Requires two arrays of
    :code:`Cp_values` and :code:`Cp_wind_speeds`.

:code:`power_curve` : Object
    An object containing a nested dictionary of power performance characteristics. Requires two arrays of
    :code:`power_values` and :code:`power_wind_speeds`.

:code:`Ct_curve` : Object
    An object containing a nested dictionary of Cp performance characteristics. Requires two arrays of
    :code:`Ct_values` and :code:`Ct_wind_speeds`.

:code:`rated_wind_speed` : Number
    A number specifying the rated wind speed of the turbine in m/s.

:code:`cutin_wind_speed` : Number
    A number specifying the cut-in wind speed of the turbine in m/s.

:code:`cutout_wind_speed` : Number
    A number specifying the cut-out wind speed of the turbine in m/s.

:code:`rated_power` : Number
    A number specifying the rated power of the turbine in W.

.. _wind_farm_examples:

Examples
========

Both :ref:`Farm Examples` and :ref:`Turbine Examples` are included below.

Farm Examples
-------------

Three farm examples are shown below, all taken from the IEA Wind Task 37 Layout Optimization Case Studies.
Details of the case studies are given `here <https://github.com/IEAWindSystems/iea37-wflo-casestudies>`_.

IEA Wind Task 37 Case study 1+2, 16WT Wind Farm
```````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 1+2, 16WT Wind Farm is defined.

.. literalinclude:: ../../windIO/examples/plant/plant_wind_farm/IEA37_case_study_1_2_wind_farm.yaml
    :start-at: name:
    :end-at: rotor_diameter:

IEA Wind Task 37 Case study 3, 25WT Wind Farm
```````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 3, 25WT Wind Farm is defined.

.. literalinclude:: ../../windIO/examples/plant/plant_wind_farm/IEA37_case_study_3_wind_farm.yaml
    :start-at: name:
    :end-at: turbines:

IEA Wind Task 37 Case study 4, 81WT Wind Farm
```````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 4, 81WT Wind Farm is defined.

.. literalinclude:: ../../windIO/examples/plant/plant_wind_farm/IEA37_case_study_4_wind_farm.yaml
    :start-at: name:
    :end-at: turbines:

Turbine Examples
----------------

Three IEA Wind Task 37 reference turbine definitions are given below as examples of how to define turbines
within the wind plant schema.

IEA Wind Task 37 3.35MW Reference Turbine
``````````````````````````````````````````

In this example, the IEA 37 3.35MW reference turbine is specified using the rated power, rated/cut-in/cut-out
wind speeds, the Ct curve, hub height, and rotor diameter.

.. literalinclude:: ../../windIO/examples/plant/plant_energy_turbine/IEA37_3.35MW_turbine.yaml
    :start-at: name:
    :end-at: rotor_diameter:

IEA Wind Task 37 10MW Reference Turbine
``````````````````````````````````````````

In this example, the IEA 37 10MW reference turbine is specified using the rated power, rated/cut-in/cut-out
wind speeds, the Ct curve, hub height, and rotor diameter.

.. literalinclude:: ../../windIO/examples/plant/plant_energy_turbine/IEA37_10MW_turbine.yaml
    :start-at: name:
    :end-at: rotor_diameter:

IEA Wind Task 37 15MW Reference Turbine
``````````````````````````````````````````

In this example, the IEA 37 15MW reference turbine is specified using the Cp/Ct curves, 
hub height, and rotor diameter.

.. literalinclude:: ../../windIO/examples/plant/plant_energy_turbine/IEA37_15MW_turbine.yaml
    :start-at: name:
    :end-at: rotor_diameter:
