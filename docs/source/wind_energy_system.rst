Wind Energy System
==================

The wind energy system defintion is the highest level definition in the plant onotology.
Required properties include :code:`name`, :code:`site`, and :code:`wind_farm`. For specific details
on the properties, see :ref:`below <wind_energy_system_properites>`

.. literalinclude:: ../../windIO/examples/plant/wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml
    :start-at: name: IEA Wind Task 37 Case study 1+2, 16WT Wind Energy System
    :end-at: name: Bastankhah’s Gaussian wake model (simplified version) 

.. _wind_energy_system_properites:

Properties
----------

:code:`name` : String
    Unique identifier of the wind energy system.

:code:`site` : Object
    Nested dictionary structure of components composing the site. For specific details on site parameters, see :ref:`site`.

:code:`wind_farm` : Object
    Nested dictionary structure of components composing the wind farm. For specific details on site parameters, see :ref:`Wind Farm`.

:code:`attributes` : Object
    Nested dictionary structure of calculated values and relavent details of the wind energy system.

:code:`optimisation` : Object
    Nested dictionary structure of optimisation information.

.. _wind_energy_system_examples:

Examples
--------

IEA Wind Task 37 Case Study 1 & 2
`````````````````````````````````

In this example, the IEA 37 Case Study 1 & 2 system definitions are given.

.. literalinclude:: ../../windIO/examples/plant/wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml
    :start-at: name: IEA Wind Task 37 Case study 1+2, 16WT Wind Energy System
    :end-at: name: Bastankhah’s Gaussian wake model (simplified version) 

IEA Wind Task 37 Case Study 3
`````````````````````````````

In this example, the IEA 37 Case Study 3 system definition is given.

.. literalinclude:: ../../windIO/examples/plant/wind_energy_system/IEA37_case_study_3_wind_energy_system.yaml
    :start-at: name: IEA Wind Task 37 Case study 3, 25WT Wind Farm
    :end-at: name: Bastankhah’s Gaussian wake model (simplified version) 

IEA Wind Task 37 Case Study 4
`````````````````````````````

In this example, the IEA 37 Case Study 4 system definition is given.

.. literalinclude:: ../../windIO/examples/plant/wind_energy_system/IEA37_case_study_4_wind_energy_system.yaml
    :start-at: name: IEA Wind Task 37 Case study 4, 81WT Wind Farm
    :end-at: name: Bastankhah’s Gaussian wake model (simplified version) 
