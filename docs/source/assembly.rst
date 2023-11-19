*******************
Assembly
*******************

The field :code:`assembly` includes five entries that aim at describing the overall configuration of the wind turbine:

.. literalinclude:: ../../test/turbine/IEA-15-240-RWT.yaml
    :start-after: assembly
    :end-before: control

:code:`turbine_class` : String 
    IEA wind class. The entry should be :code:`I`, :code:`II`, :code:`III`, or :code:`IV`. 

:code:`turbulence_class` : String 
    IEA turbulence class. The entry should be :code:`A`, :code:`B`, or :code:`C`. 

:code:`drivetrain` : String 
    Drivetrain configuration. This is intended to inform a automated interpreter of the yaml about the data specified in the field :code:`drivetrain`

:code:`rotor_orientation` : String 
    Switch between :code:`upwind` and :code:`downwind` rotor configurations.

:code:`number_of_blades` : Integer 
    Number of rotor blades.
