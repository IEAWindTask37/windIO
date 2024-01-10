Site
****

The site schema details the characteristics related to the physical site that the wind energy system
is located at. These include human-defined properties such as wind enery area boundaries as well as
natural phenomena, such as the wind energy resource available at the site. For the schema, required
properties include :code:`name`, :code:`boundaries`, and :code:`energy_resource`. For details on the
properites, see :ref:`below <site_properties>`

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_1_2_energy_site.yaml
    :start-at: name:
    :end-at: energy_resource:

.. _site_properties:

Properties
==========

:code:`name` : String
    Unique identifier of the wind energy site.

:code:`boundaries` : Object
    Nested dictionary structure of components composing the boundary of the site.
    Requires either a :code:`polygons` or a :code:`circle` definition. :code:`polygons` is an
    object that contains an array of vertices that define a polygon shape.
    Multiple arrays can be supplied to represent multiple polygon boundaries.
    A :code:`circle` object requires the center coordinates and the radius of the
    circle boundary. Examples of a :code:`polygons` and a :code:`circle` definition are
    given below.

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_1_2_energy_site.yaml
    :start-after: name:
    :end-before: energy_resource:

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_4_energy_site.yaml
    :start-after: name:
    :end-before: energy_resource:

:code:`exclusions` : Object
    Nested dictionary structure of components composing the exclusions within a site.
    Requires either a :code:`polygons` or a :code:`circle` definition, the same
    as :code:`boundaries`.

:code:`energy_resource` : Object
    Nested dictionary structure of components composing the energy resource for the site.
    For specific details on site parameters, see :ref:`energy_resource`.

:code:`bathymetry` : Object
    The bathymetry of a site describes the variations in depth in a water body at the wind energy system's location. It can be an essential aspect when considering offshore wind farms, as it can influence the design, placement, and feasibility of the turbine foundation. The bathymetry is defined with two components:

    :code:`coordinates` : Array of Objects
        An array representing the x and y coordinates associated with different depths. These coordinates describe the points in a grid or mesh that maps the underwater terrain.

    :code:`depth` : Array of Numbers
        An array representing the depth values at corresponding coordinates, measured in meters.


.. _site_examples:

Examples
========

Three plant energy site examples are shown below, all taken from the IEA Wind Task 37 Layout Optimization
Case Studies. Details of the case studies are given
`here <https://github.com/IEAWindTask37/iea37-wflo-casestudies>`_.

IEA Wind Task 37 Case study 1+2, 16WT Plant Energy Site
```````````````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 1+2, 16WT Plant Energy Site is defined.

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_1_2_energy_site.yaml
    :start-at: name:
    :end-at: energy_resource:

IEA Wind Task 37 Case study 3, 25WT Plant Energy Site
`````````````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 3, 25WT Plant Energy Site is defined.

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_3_energy_site.yaml
    :start-at: name:
    :end-at: energy_resource:

IEA Wind Task 37 Case study 4, 81WT Plant Energy Site
`````````````````````````````````````````````````````

In this example, the IEA Wind Task 37 Case study 4, 81WT Plant Energy Site is defined.

.. literalinclude:: ../../examples/plant/plant_energy_site/IEA37_case_study_4_energy_site.yaml
    :start-at: name:
    :end-at: energy_resource:
