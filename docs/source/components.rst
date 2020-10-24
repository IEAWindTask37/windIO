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

:code:`airfoil_position'labels` : Array of strings 
    The array :code:`labels` specifies the names of the airfoils to be placed along the blade. The positions are specified in the field :code:`grid`. The two arrays must share the same length and to keep an airfoil constant along blade span, this must be defined twice. The :code:`labels` must match the :code:`names` of the airfoils listed in the top level :code:`airfoils`.

:code:`chord.values` : Array of floats, m 
    The array :code:`values` specifies the chord along blade span.

:code:`twist.values` : Array of floats, rad 
    The array :code:`values` specifies the aerodynamic twist along blade span. In the example provided above, a json pointer &twist is defined, which will be used to rotate composite layers in :code:`internal_structure_2d_fem`. Remember, the unit of measure of the twist is not degrees!

:code:`pitch_axis.values` : Array of floats 
    The array :code:`values` specifies the positions along blade span of the position of the airfoil in respect to the blade reference axis. A value of 0 means that the reference axis, around which the blade pitches and twists, crosses the airfoil at the leading edge, while a value of 1 corresponds to the trailing edge. Standard value oscillate between 0.5 for the blade root cylinder and 0.25. These are the values reported in the example.

:code:`reference_axis` : Object
    The field :code:`reference_axis` describe the three-dimensional shape of the reference axis of the blade via three sub-fields, namely :code:`x`, :code:`y`, and :code:`z`. The three sub-fields contain the pairs of arrays :code:`grid` and :code:`values`. The former is nondimensional, while the latter is expressed in meters.

    The coordinate system is the one of `BeamDyn  <https://openfast.readthedocs.io/en/master/source/user/beamdyn/input_files.html#beamdyn-primary-input-file>`_ of OpenFAST and it is shown in the figure below. 

    .. image:: images/reference_axis.jpg
        :width: 800
    
    The consequences of this reference system is that standard wind turbine blades have positive twist inboard and close to zero or even slightly negative twist outboard, zero or negative x values for standard prebent blades, and positive y values for backward swept blades. The blade main direction is expressed along z, and total blade length must be computed integrating the fields x, y, and z three-dimensionally.



elastic properties mb 
-----------------------
The equivalent elastic properties of the blade are defined in :code:`elastic_properties_mb`. Here, 6x6 stiffness and mass matrices are defined in the same reference system used by the solver `BeamDyn  <https://openfast.readthedocs.io/en/master/source/user/beamdyn/input_files.html#beamdyn-primary-input-file>`_ of OpenFAST. Out of 36 entries of the matrices, given the symmetry, the yaml file requires the definition of only 21 values as inputs. These are defined row by row, so first the six elements of the first row, then the five elements of the second row, and so on finishing with the sixth element of the sixth row.
For a blade without extra-diagonal, the stiffness and mass matrices look like this:

K = [Kflap, 0, 0, 0, 0, 0, Kedge, 0, 0, 0,0, EA, 0, 0, 0, EIedge, 0, 0, EIflap, 0, GJ]

M = [m, 0, 0, 0, 0, -mYcm, m, 0, 0, 0,mXcm, m, mYcm, -mXcm, 0, iedge, -icp, 0, iflap, 0, iplr]

where KShrEdg and KShrFlp are the edge and flap shear stiffnesses, respectively; EA is the extension stiffness; EIEdg and EIFlp are the edge and flap stiffnesses, respectively; GJ is the torsional stiffness, m is the mass density per unit span, Xcm and Ycm are the local coordinates of the sectional center of mass, iedge and iflap are the edge and flap mass moments of inertia per unit span, iplr is the polar moment of inertia per unit span, and finally icp is the sectional cross product of inertia per unit span. Please note that for beam-like structures iplr must be equal to iedge plus iflap.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Blade - Elastic properties
    :end-before: # Internal Structure 2D FEM

internal structure 2d_fem
---------------------------
The field :code:`internal_structure_2d_fem` contains the data to describe the internal structure of standard wind turbine blades. This is a fairly sophisticated process and the ontology proposed in this work supports different definitions. On the top level, the field :code:`internal_structure_2d_fem` has three sub-components, namely the :code:`reference_axis`, which is usually defined equal to the :code:`reference_axis` in the field :code:`outer_shape_bem`, the :code:`webs`, where the positions of the shear webs are defined, and the :code:`layers`, which describe all internal layers in terms of :code:`name`, :code:`material`, :code:`thickness`, number of plies :code:`n_plies`, :code:`fiber_orientation` (for composites), and position in the two-dimensional sections. 

.. literalinclude:: ../../test/top_level.yaml
    :start-after: # Structure
    :end-before: # EOF3


webs
^^^^^^^^^^
The field :code:`webs` consists of a list of entries, each representing a shear web defined in terms of :code:`name` and position.

:code:`name` : String
    String that identifies the web.

The first (and usually most convenient) way to define the position of a shear web is by defining the fields :code:`rotation` and :code:`offset_y_pa`, which are distributed along span and are therefore described in terms of :code:`grid` and :code:`values` pairs.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Webs
    :end-before: # Web 2

:code:`rotation.values` : Array of floats, rad 
    The rotation defines the angle between the chord line and the y axis and it has the opposite sign of the twist. For shear webs perpendicular to the chord line in the section(s) where twist is zero, it is easiest to simply use the keyword fixed: twist. In the example provided above, a json pointer &twist is defined.
    
:code:`offset_y_pa.values` : Array of floats, m 
    The field offset_y_pa defines the distance in meters along the y axis between the pitch axis and the plane of the shear web and it is defined along y. 


Blades with straight shear webs will always have the field rotation equal to the twist plus/minus a constant angle and, assuming a non-swept blade (zero values in the blade y reference axis), a linear field offset_y_pa.

    .. image:: images/web1.jpg
        :width: 800

The second approach to define the position of a shear web is by defining the fields :code:`start_nd_arc` and :code:`end_nd_arc`, which are also distributed along span and are therefore also described in terms of :code:`grid` and :code:`values` pairs.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Web 2
    :end-before: # Layers

:code:`start_nd_arc.values` : Array of floats
    The field defines the nondimensional position along the arc of a 2D blade section, where 0 represents the trailing edge on the suction side and 1 the trailing edge on the pressure side. For flatback airfoils, the start (s = 0) and end (s = 1) nondimensional coordinate s is defined in the midpoint between suction and pressure sides. The shear webs have the field :code:`start_nd_arc` on the suction side, so usually smaller than 0.5, which approximately correspond to the leading edge.
    
:code:`end_nd_arc.values` : Array of floats
    On the opposite, the shear webs have the field :code:`end_nd_arc` on the pressure side, so usually between 0.5 and 1.
     
    .. image:: images/web2.jpg
        :width: 400



layers
^^^^^^^^^^^^^
The sub-field :code:`layers` define the layers of the wind turbine blade. In most cases, these are layers of composite materials. Each layer is defined by the following entries.

:code:`name` : String
    String that identifies the layer.
:code:`material` : String
    String that identifies the material of the layer. The material and its properties must be defined in the top-level :code:`materials`.
:code:`thickness` : Float, m
    Dimensional thickness of the laminate, expressed in meters. This value is modeled constant along the section. To define ply drops along the 2D surface, the user is therefore required to define multiple layers, possibly ply by ply when many ply drops exist.
:code:`n_plies` : Float
    In addition or in alternative to the dimensional thickness, the discrete number of plies of a composite laminate can be defined by the user. Notably, the ply thickness is a material property (not a layer property) and it is defined in the top-level field materials.
:code:`fiber_orientation` : Float, rad
    For composite laminates, the orientation of the fibers in radians can be specified. Looking from blade root, positive angles represent a rotation of the fibers towards the leading edge of the blade.

The position of the layer in the 2D section can be specified in various ways. If nothing is defined, this assumes that the sub-field :code:`start_nd_arc` is equal to 0 and the sub-field :code:`end_nd_arc` is equal to 1. This means that the layer wraps the whole section, such as in the example below for the outer paint. This definition of a layer should be used also for example for the outer shell skin, which tyoically wraps the whole section.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Layer 1
    :end-before: # Layer 2

The most convenient approach to define the position of spar caps mimics the definition of the shear webs, adding the width and side that define the width of the layer in meters and the side where the layer is located, either “pressure” or “suction”. 

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Layer 3
    :end-before: # Layer 4

:code:`width.values` : Array of floats, m 
    The field width defines the width in meters along the arc of the layer. 

:code:`side` : String
    The field side is string that can be either :code:`suction` or :code:`pressure`, defining the side where a layer is defined.

    .. image:: images/layer1.jpg
        :width: 800

To define reinforcements, the best way is usually to define the width, in meters, and the midpoint, named :code:`midpoint_nd_arc` and defined nondimensional between 0 and 1. Converters should be able to look for the leading edge, marked as LE.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Layer 4
    :end-before: # Layer 5

:code:`midpoint_nd_arc.values` : Array of floats
    Coordinate along the arc of the midpoint of the layer. 

Similar combinations can be constructed with the combination of :code:`width` and :code:`start_nd_arc` or :code:`end_nd_arc`.

    .. image:: images/layer2.jpg
        :width: 800

Finally, for composite layers belonging to the shear webs, a tag :code:`web` should contain the name of the web. The layers are then modeled from leading edge to trailing edge in the order they were specified.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Web layer
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
    Mass moments of inertia of the hub system. Ixx, Iyy, Izz, Ixy, Ixz, Iyz are expressed around the hub center in hub-aligned coordinate system, which has x aligned with the main shaft pointing from the rotor apex towards the nacelle. Iyy and Izz are usually identical.

:code:`system_center_mass` : Array (3) of floats, m
    Coordinates of the center of mass of the hub. Work in progress.


Nacelle
================

The field :code:`nacelle` describes the nacelle system from an aeroelastic perspective, distinguishing between aerodynamic and elastic properties, added in the fields :code:`outer_shape_bem` and :code:`elastic_properties_mb` respectively. An addition field :code:`drivetrain` is optional and defines some of the inputs used to size the drivetrain components.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Nacelle
    :end-before: # end nacelle

:code:`uptilt_angle` : Float, rad
    Angle between the main shaft and the horizontal plane. This is defined positive for standard upwind and downwind turbines.

:code:`distance_tt_hub` : Float, m
    Vertical distance between the top of the tower and the hub center.

:code:`overhang` : Float, m
    Horizontal distance between the axis of the tower and the hub center.

:code:`length` : Float, m
    Length of the nacelle, defined along the main shaft.

:code:`height` : Float, m
    Height of the nacelle, defined along the direction perpendicular to the main shaft.

:code:`width` : Float, m
    Width of the nacelle, defined horizontal and perpendicular to the main shaft.

:code:`drag_coefficient` : Float
    This is the equivalent drag coefficient used to compute the aerodynamic forces generated by the nacelle immersed in the flow. Standard aeroelastic solvers use this parameter.

:code:`above_yaw_mass` : Float, kg
    This is the overall mass of the nacelle system, which includes the main shaft, the drivetrain system, the generator, the nacelle cover, etc. This does not include the yaw system.

:code:`yaw_mass` : Float, kg
    Mass of the yaw system.

:code:`center_mass` : Float, m
    These are the coordinates of the center of mass of the nacelle, defined in yaw-aligned coordinate system, which has x horizontal pointing downwind, y horizontal pointing laterally, and z pointing vertically upwards.

:code:`inertia` : Array (6) of floats, kg*m2
    Mass moments of inertia of the nacelle system. Ixx, Iyy, Izz, Ixy, Ixz, Iyz are expressed in the yaw-aligned coordinate system.

Tower
================

The :code:`tower` is defined similar to the :code:`blade`.

:code:`reference_axis` : Object
    The field :code:`reference_axis` describe the three-dimensional shape of the reference axis of the tower via three sub-fields, namely :code:`x`, :code:`y`, and :code:`z`. The three sub-fields contain the pairs of arrays :code:`grid` and :code:`values`. The former is nondimensional, while the latter is expressed in meters. :code:`x`, :code:`y`, and :code:`z` are expressed in the tower reference system, with :code:`x` parallel to the ground pointing downwind, :code:`y` parallel to the ground and to the rotor plane, and :code:`z` perpendicular to the ground pointing upwards. Standard towers are only defined along :code:`z`.

:code:`outer_diameter.values` : Array of floats, m
    Diameters of the tower defined from tower base (grid = 0) to tower top (grid = 1).

:code:`drag_coefficient.values` : Array of floats
    This is the equivalent drag coefficient used to compute the aerodynamic forces generated by the tower immersed in the flow. Standard aeroelastic solvers use this parameter.

:code:`outfitting_factor` : Float
    Multiplier of tower mass to account for the mass of the auxiliary systems, such as stairs, elevator, paint, etc. This can be used to convert the mass of the steel cylinders to the total mass of the tower.

The field :code:`layers` mimic the same field of the blade.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Tower
    :end-before: # Foundation

Foundation
================
So far, :code:`foundation` is the simplest component with a single input describing the height of the foundation.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Foundation
    :end-before: # RNA

:code:`height` : Float, m 
    Height of the foundation. Distance between ground and tower base.

RNA
================
The equivalent elastic properties of the rotor-nacelle assembly are work in progress.
    :start-after: # RNA
    :end-before: # Airfoils




Floating Platform
========================================
The floating platform ontology uses a *graph*-like representation of the geometry with Joints and Members.  Additional rigid body point masses can be defined at the joints as well.


Joints
----------------------------------------
Joints are the *nodes* of the graph representation of the floating platform.  They must be assigned a unique name for later reference by the Members.


:code:`name` : String
    Unique name of the joint (node)

:code:`location` : Array of Floats, m
    x, y, and z coordinates of this node in the global coordinate
    system.

:code:`transition` : Boolean
    Whether the transition piece and turbine tower attach at this node

    *Default* = False

:code:`reactions.Rx` : Boolean
    True if this joint is compliant in *x-translation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True
    
    *Default* = False

:code:`reactions.Ry` : Boolean
    True if this joint is compliant in *y-translation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True

    *Default* = False

:code:`reactions.Rz` : Boolean
    True if this joint is compliant in *z-translation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True

    *Default* = False

:code:`reactions.Rxx` : Boolean
    True if this joint is compliant in *x-rotation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True

    *Default* = False

:code:`reactions.Ryy` : Boolean
    True if this joint is compliant in *y-rotation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True

    *Default* = False

:code:`reactions.Rzz` : Boolean
    True if this joint is compliant in *z-rotation* in the member coordinate system,
    False if this joint is completely rigid in that direction.  For instance, a perfect
    ball joint would be Rx=Ry=Rz=False, Rxx=Ryy=Rzz=True

    *Default* = False

:code:`reactions_global.Euler` : Array of Floats
    Euler angles [alpha, beta, gamma] that describe the rotation of
    the Reaction coordinate system relative to the global coordinate
    system α is a rotation around the z axis, β is a rotation around
    the x' axis, γ is a rotation around the z" axis.


Members
----------------------------------------

:code:`name` : String
    Name of the member

:code:`joint1` : String
    Name of joint/node connection

:code:`joint2` : String
    Name of joint/node connection


:code:`hydrodynamic_approach` : String from, ['strip', 'potential', 'both']
    (Optional) How should this member be modeled?

    *Default* = strip

:code:`Ca` : Float
    (Optional) Added mass coefficient

    *Default* = 0.0

:code:`Cp` : Float
    (Optional) Pressure coefficient

    *Default* = 0.0

:code:`Cd` : Float
    (Optional) Drag coefficient

    *Default* = 0.0
    
:code:`outer_shape.shape` : String from, ['circular', 'polygonal']
    Specifies cross-sectional shape of the member.  If circular, then the
    :code:`outer_diameter` field is required.  If polygonal, then the :code:`side_lengths`,
    :code:`angles`, and :code:`rotation` fields are required

:code:`outer_shape.outer_diameter.grid` : Array of floats, m
    Non-dimensional points along member axis from 0.0 at :code:`joint1` to 1.0 at :code:`joint2`
    at which the diameter is defined

:code:`outer_shape.outer_diameter.values` : Array of floats, m
    Diameters of the member defined at the non-dimensional grid points

:code:`outer_shape.side_lengths1` : Array of Floats, m
    Polygon side lengths at joint1

    *Minimum* = 0

:code:`outer_shape.side_lengths2` : Array of Floats, m
    Polygon side lengths at joint1

    *Minimum* = 0

:code:`outer_shape.angles` : Array of Floats, rad
    Polygon angles with the ordering such that angle[i] is between
    side_length[i] and side_length[i+1]

    *Minimum* = 0

:code:`outer_shape.rotation` : Float, rad
    Angle between principle axes of the cross-section and the member
    coordinate system.  Essentially the rotation of the member if both
    joints were placed on the global x-y axis with the first side
    length along the z-axis

:code:`internal_structure.outfitting_factor` : Float
    Scaling factor for the member mass to account for auxiliary
    structures, such as elevator, ladders, cables, platforms,
    fasteners, etc

    *Default* = 1.0

    *Minimum* = 1.0

:code:`internal_structure.layers.name` : String
    structural component identifier

:code:`internal_structure.layers.material` : String
    material identifier

:code:`internal_structure.layers.thickness.grid` : Array of floats, m
    Non-dimensional points along member axis from 0.0 at :code:`joint1` to 1.0 at :code:`joint2`
    at which the thickness is defined

:code:`internal_structure.layers.thickness.values` : Array of floats, m
    Thickness of the member defined at the non-dimensional grid points

:code:`internal_structure.bulkhead.material` : String
    material identifier for the bulkheads

:code:`internal_structure.bulkhead.grid` : Array of floats
    Non-dimensional points along member axis from 0.0 at :code:`joint1` to 1.0 at :code:`joint2`
    where bulkheads are located

:code:`internal_structure.bulkhead.values` : Array of floats, m
    Bulkhead thickness defined at the non-dimensional grid points

:code:`internal_structure.ballast.variable_flag` : Boolean
    If true, then this ballast is variable and adjusted by control
    system.  If false, then considered permanent and the :code:`material` and
    :code:`volume` entries are required

:code:`internal_structure.ballast.material` : String
    Material identifier

:code:`internal_structure.ballast.volume` : Float, m^3
    Total volume of ballast (permanent ballast only)

    *Minimum* = 0


Stiffeners
^^^^^^^^^^^
Both internal :code:`ring_stiffeners` and :code:`longitudinal_stiffeners` can be specified with the :code:`internal_structure` section of a Member.  Stiffeners are defined by their material and 4 dimensions, illustrated in this diagram,

    .. image:: images/stiffenerZoom.png
        :width: 200

:code:`material` : String
    material identifier

:code:`flange_height` : Float, m

    *Minimum* = 0

:code:`flange_width` : Float, m


    *Minimum* = 0

:code:`web_height` : Float, m


    *Minimum* = 0

:code:`web_thickness` : Float, m


    *Minimum* = 0


axial_joints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Additional joints that are defined along the non-dimensional member axis can be defined here.  Unlike the joints defined in the global coordinate system in the :code:`joints` section of the ontology, these joints will change their absolute (x,y,z) location if the member diameter is altered the or :code:`joint1` or :code:`joint2` locations are changed during an optimization.  This is especially useful when designing a truss-like structure with pontoons attaching to primary members or columns in a semisubmersible. Like the joints above, these must be given a unique name.

:code:`name` : String
    Unique name of joint

:code:`grid` : Float
    Non-dimensional value along member axis

    *Minimum* = 0.0    *Maximum* = 1.0


Rigid bodies
----------------------------------------
There is an allowance for additional point masses at joints with user-customized properties.  This would be useful in modeling ???.

:code:`joint1` : String
    Name of joint/node connection

:code:`mass` : Float, kg
    Mass of this rigid body

    *Minimum* = 0

:code:`cost` : Float, USD
    Cost of this rigid body

    *Minimum* = 0

:code:`cm_offset` : Array of Floats, m
    Offset from joint location to center of mass (CM) of body in dx,
    dy, dz

:code:`moments_of_inertia` : Array of Floats, kg*m^2
    Moments of inertia around body CM in Ixx, Iyy, Izz

    *Minimum* = 0

:code:`hydrodynamic_approach` : String from, ['strip', 'potential', 'both']
    How should this member be modeled?

    *Default* = strip

:code:`Ca` : Float
    Added mass coefficient

    *Default* = 0.0

:code:`Cp` : Float
    Pressure coefficient

    *Default* = 0.0

:code:`Cd` : Float
    Drag coefficient

    *Default* = 0.0



Mooring
========================================
The mooring system ontology follows closely the input file format for MoorDyn or MAP++.  Additional information can be found in the `MoorDyn user guide <http://www.matt-hall.ca/files/MoorDyn-Users-Guide-2017-08-16.pdf>`_ .

nodes
-------------

:code:`name` : String
    Name or ID of this node for use in line segment

:code:`node_type` : String from, ['fixed', 'connection', 'vessel']


:code:`location` : Array of Floats, meter
    – Coordinates x, y, and z of the connection (relative to inertial
    reference frame if Fixed or Connect, relative to platform
    reference frame if Vessel). In the case of Connect nodes, it is
    simply an initial guess for position before MoorDyn calculates the
    equilibrium initial position.

:code:`anchor_type` : String
    Name of anchor type from anchor_type list

:code:`fairlead_type` : String from, ['rigid', 'actuated', 'ball']


:code:`node_mass` : Float, kilogram
    Clump weight mass

    *Minimum* = 0.0

:code:`node_volume` : Float, meter^3
    Floater volume

    *Minimum* = 0.0

:code:`drag_area` : Float, meter^2
    Product of drag coefficient and projected area (assumed constant
    in all directions) to calculate a drag force for the node

    *Minimum* = 0.0

:code:`added_mass` : Float
    Added mass coefficient used along with node volume to calculate
    added mass on node



lines
-------------

:code:`name` : String
    ID of this line

:code:`line_type` : String
    Reference to line type database

:code:`unstretched_length` : Float, meter
    length of line segment prior to tensioning

    *Minimum* = 0.0

:code:`node1` : String
    node id of first line connection

:code:`node2` : String
    node id of second line connection



line_types
-------------

:code:`name` : String
    Name of material or line type to be referenced by line segments

:code:`diameter` : Float, meter
    the volume-equivalent diameter of the line – the diameter of a
    cylinder having the same displacement per unit length

    *Minimum* = 0.0

:code:`mass_density` : Float, kilogram/meter
    mass per unit length (in air)

    *Minimum* = 0.0

:code:`stiffness` : Float, Newton
    axial line stiffness, product of elasticity modulus and cross-
    sectional area

    *Minimum* = 0.0

:code:`cost` : Float, USD/meter
    cost per unit length

    *Minimum* = 0.0

:code:`breaking_load` : Float, Newton
    line break tension

    *Minimum* = 0.0

:code:`damping` : Float, Newton * second
    internal damping (BA)

:code:`transverse_added_mass` : Float
    transverse added mass coefficient (with respect to line
    displacement)

    *Minimum* = 0.0

:code:`tangential_added_mass` : Float
    tangential added mass coefficient (with respect to line
    displacement)

    *Minimum* = 0.0

:code:`transverse_drag` : Float
    transverse drag coefficient (with respect to frontal area, d*l)

    *Minimum* = 0.0

:code:`tangential_drag` : Float
    tangential drag coefficient (with respect to surface area, π*d*l)

    *Minimum* = 0.0



anchor_types
-------------

:code:`name` : String
    Name of anchor to be referenced by anchor_id in Nodes section

:code:`mass` : Float, kilogram
    mass of the anchor

    *Minimum* = 0.0

:code:`cost` : Float, USD
    cost of the anchor

    *Minimum* = 0.0

:code:`max_lateral_load` : Float, Newton
    Maximum lateral load (parallel to the sea floor) that the anchor
    can support

    *Minimum* = 0.0

:code:`max_vertical_load` : Float, Newton
    Maximum vertical load (perpendicular to the sea floor) that the
    anchor can support

    *Minimum* = 0.0
		 
