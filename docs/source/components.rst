*******************
Components
*******************

The inputs describing the wind turbine components are described here. The ontology windIO currently distinguishes the five components :code:`blade`, :code:`hub`, :code:`nacelle`, :code:`tower`, and :code:`foundation`

.. literalinclude:: ../../test/top_level.yaml
    :start-after: # Components
    :end-before: # EOF2

Blade
================
The component :code:`blade` includes three subcomponents

Aerodynamics 
-------------------
:code:`outer_shape_bem` consists of a dictionary containing the data for blade BEM-based aerodynamics

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Blade - Outer Shape BEM
    :end-before: # Blade - Elastic properties

:code:`airfoil_position` : Object 
    The field includes a nondimensional :code:`grid`, ranging from 0 (blade root) to 1 (blade tip), specifying the positions of airfoils along the curved blade axis. The names of the airfoils are specified in the list of strings :code:`labels`. The two arrays must share the same length. The :code:`labels` must match the :code:`names` of the airfoils listed in the top level :code:`airfoils`.

Elastic Properties 
-------------------
:code:`elastic_properties_mb` consists of a dictionary containing the elastic equivalent properties of multiple beam models for the blade

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Blade - Elastic properties
    :end-before: # Internal Structure 2D FEM

Internal Structure
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

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Hub
    :end-before: # Nacelle

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