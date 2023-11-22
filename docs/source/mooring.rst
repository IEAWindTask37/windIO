Mooring
========================================
The mooring system ontology follows closely the input file format for MoorDyn or MAP++.  Additional information can be found in the `MoorDyn user guide <http://www.matt-hall.ca/files/MoorDyn-Users-Guide-2017-08-16.pdf>`_ .

.. literalinclude:: ../../test/turbine/IEA-15-240-RWT_VolturnUS-S.yaml
    :start-after: mooring
    :end-before: airfoils

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
