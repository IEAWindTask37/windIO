Control
------------

The data describing the wind turbine controller are included in the field :code:`control`.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Control
    :end-before: # Environment

:code:`rated_power` : Float, W
    Rated electrical power of the generator
:code:`Vin` : Float, m/s
    Cut in wind speed
:code:`Vout` : Float, m/s
    Cut out wind speed
:code:`minOmega` : Float, rad/s
    Minimum rotor speed
:code:`maxOmega` : Float, rad/s
    Maximum rotor speed
:code:`tsr` : Float
    Nominal tip speed ratio
:code:`pitch` : Float, rad
    Nominal pitch angle
:code:`maxTS` : Float, m/s
    Maximum blade tip speed
:code:`max_pitch_rate` : Float, rad/s
    Maximum pitch angle rate
:code:`max_torque_rate` : Float, Nm/s
    Maximum generator torque rate
:code:`PC_zeta` : Float
    Pitch controller damping ratio
:code:`PC_omega` : Float, rad/s
    Pitch controller natural frequency
:code:`VS_zeta` : Float
    Generator torque controller damping ratio
:code:`VS_omega` : Float, rad/s
    Generator torque controller natural frequency
:code:`max_pitch` : Float, rad
    Maximum pitch angle
:code:`min_pitch` : Float, rad
    Minimum pitch angle    
:code:`ss_vsgain` : Float
    Torque controller setpoint smoother gain bias percentage
:code:`ss_pcgain` : Float
    Pitch controller setpoint smoother gain bias percentage
:code:`ps_percent` : Float
    Percent thrust peak shaving