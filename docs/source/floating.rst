Floating Platform
========================================
The floating platform ontology uses a *graph*-like representation of the geometry with Joints and Members.  Additional rigid body point masses can be defined at the joints as well.


Joints
----------------------------------------
Joints are the *nodes* of the graph representation of the floating platform.  They must be assigned a unique name for later reference by the Members.

.. literalinclude:: ../../test/turbine/IEA-15-240-RWT_VolturnUS-S.yaml
    :start-after: floating_platform
    :end-before: members


:code:`name` : String
    Unique name of the joint (node)

:code:`location` : Array of Floats, m
    Coordinates (x,y,z or r,θ,z) of the joint in the global coordinate system.

:code:`transition` : Boolean
    Whether the transition piece and turbine tower attach at this node

    *Default* = False

:code:`cylindrical` : Boolean
    Whether to use cylindrical coordinates (r,θ,z), with (r,θ) lying in the x/y-plane, instead of Cartesian coordinates.

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

.. literalinclude:: ../../test/turbine/IEA-15-240-RWT_VolturnUS-S.yaml
    :start-after: members
    :end-before: mooring

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
Both internal :code:`ring_stiffeners` and :code:`longitudinal_stiffeners` can be specified with the :code:`internal_structure` section of a Member.  Stiffeners are defined by their material, spacing, and 4 dimensions, illustrated in this diagram,

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

:code:`spacing` : Float, m
    Spacing between stiffeners in non-dimensional grid coordinates. Value of 1.0 means no stiffeners

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

.. .. literalinclude:: ../../test/turbine/IEA-15-240-RWT_VolturnUS-S.yaml
..     :start-after: # Rigid
..     :end-before: # Mooring

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