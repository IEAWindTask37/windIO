*******************
Components
*******************

The inputs describing the wind turbine components are described here. The ontology windIO currently distinguishes the five components :code:`blade`, :code:`hub`, :code:`nacelle`, :code:`tower`, and :code:`foundation`

.. literalinclude:: ../../test/top_level.yaml
    :start-after: # Components
    :end-before: # EOF2



Blade
================
The component :code:`blade` includes three subcomponents, namely :code:`outer_shape_bem`, :code:`elastic_properties_mb`, and :code:`internal_structure_2d_fem`. A fourth subfield :code:`lofted_shape` is in progress.

All distributed quantities, such as blade chord or the thickness of a structural component, are expressed in terms of pair arrays :code:`grid` and :code:`values`, which must have a minimum length of two elements and the same size. :code:`grid` is defined nondimensional between 0 (root) and 1 (tip) along the, possibly curved, :code:`reference_axis`.

outer_shape_bem 
-------------------
:code:`outer_shape_bem` consists of a dictionary containing the data for blade BEM-based aerodynamics. 

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Blade - Outer Shape BEM
    :end-before: # Blade - Elastic properties

:code:`airfoil_position` : String 
    The array :code:`labels` specifies the names of the airfoils to be placed along the blade. The positions are specified in the field :code:`grid`. The two arrays must share the same length and to keep an airfoil constant along blade span, this must be defined twice. The :code:`labels` must match the :code:`names` of the airfoils listed in the top level :code:`airfoils`.

:code:`chord.values` : Array of floats, m 
    The array :code:`values` specifies the chord along blade span.

:code:`twist.values` : Array of floats, rad 
    The array :code:`values` specifies the aerodynamic twist along blade span. In the example provided above, a json pointer &twist is defined, which will be used to rotate composite layers in :code:`internal_structure_2d_fem`. Remember, the unit of measure of the twist is not degrees!

:code:`pitch_axis.values` : Array of floats 
    The array :code:`values` specifies the positions along blade span of the position of the airfoil in respect to the blade reference axis. A value of 0 means that the reference axis, around which the blade pitches and twists, crosses the airfoil at the leading edge, while a value of 1 corresponds to the trailing edge. Standard value oscillate between 0.5 for the blade root cylinder and 0.25. These are the values reported in the example.

:code:`reference_axis` : Object
    The field :code:`reference_axis` describe the three-dimensional shape of the reference axis of the blade via three sub-fields, namely :code:`x`, :code:`y`, and :code:`z`. The three sub-fields contain the pairs of arrays :code:`grid` and :code:`values`. The former is nondimensional, while the latter is expressed in meters.

    The coordinate system is the one of the OpenFAST module BeamDyn and it is shown in the figure below. 

    .. image:: images/reference_axis.jpg
        :width: 400
    
    The consequences of this reference system is that standard wind turbine blades have positive twist inboard and close to zero or even slightly negative twist outboard, zero or negative x values for standard prebent blades, and positive y values for backward swept blades. The blade main direction is expressed along z, and total blade length must be computed integrating the fields x, y, and z three-dimensionally.



elastic properties mb 
-------------------
:code:`elastic_properties_mb` consists of a dictionary containing the elastic equivalent properties of multiple beam models for the blade

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Blade - Elastic properties
    :end-before: # Internal Structure 2D FEM

internal structure 2d_fem
-------------------
:code:`internal_structure_2d_fem` consists of a dictionary containing the data describing the blade internal structure for a 2D analysis

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Internal Structure 2D FEM
    :end-before: # Hub

Lofted Shape 
-------------------
This is work in progress. :code:`lofted_shape` will consist of a dictionary containing the 3D points describing the outer lofted shape of the blade 



Hub
================
The field :code:`hub` describes the hub system from an aeroelastic perspective, distinguishing between aerodynamic and elastic properties, added in the fields :code:`outer_shape_bem` and :code:`elastic_properties_mb` respectively.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Hub
    :end-before: # Nacelle

:code:`diameter` : Float, m
    This is the outer diameter of the hub. It is also the diameter of the circle centered at the rotor apex and connecting the blade root centers.

:code:`cone_angle` : Float, rad
    This is the precone of the rotor. It is defined positive for standard upwind and downwind rotors.

:code:`drag_coefficient` : Float
    This is the equivalent drag coefficient used to compute the aerodynamic forces generated by the hub immersed in the flow. Standard aeroelastic solvers use this parameter.

:code:`system_mass` : Float, kg
    This is the overall mass of the hub system, which includes the hub itself, but also the spinner, the pitch system, the blade root bearings, and auxiliary equipment.

:code:`system_inertia` : Array (6) of floats, kg*m2
    Mass moments of inertia of the hub system. Ixx, Iyy, Izz, Ixy, Ixz, Iyz are expressed around the hub center in yaw-aligned coordinate system, which has x aligned with the main shaft pointing from the rotor apex towards the nacelle. Iyy and Izz are usually identical.

Nacelle
================

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Nacelle
    :end-before: # Tower

Tower
================

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Tower
    :end-before: # Foundation

Foundation
================
So far, :code:`foundation` is the simplest component with a single input describing the height of the foundation.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Foundation
    :end-before: # Airfoils

:code:`height` : Float, m 
    Height of the foundation. Distance between ground and tower base.