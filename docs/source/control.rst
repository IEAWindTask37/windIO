Control
------------

The data describing the wind turbine controller are included in the field :code:`control`.

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Control
    :end-before: # Environment

The entries are:
   -  :code:`rated_power`
   -  :code:`Vin`
   -  :code:`Vout`
   -  :code:`minOmega`
   -  :code:`maxOmega`
   -  :code:`tsr`
   -  :code:`pitch`
   -  :code:`maxTS`
   -  :code:`max_pitch_rate`
   -  :code:`max_torque_rate`
   -  :code:`PC_zeta`
   -  :code:`PC_omega`
   -  :code:`VS_zeta`
   -  :code:`VS_omega`
   -  :code:`max_pitch`
   -  :code:`min_pitch`
   -  :code:`vs_minspd`
   -  :code:`ss_vsgain`
   -  :code:`ss_pcgain`
   -  :code:`ps_percent`