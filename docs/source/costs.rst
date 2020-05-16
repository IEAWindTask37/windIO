Costs
------------

The field :code:`costs` includes the data to conduct an LCOE analysis of the wind turbine. The structure of the data is based on the analysis presented in the report https://www.nrel.gov/docs/fy20osti/74598.pdf

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Costs
    :end-before: # EOF

The entries are:
   -  :code:`wake_loss_factor`: Float defining the loss factor to account for wind park losses, such as wake losses. This is used to convert the annual energy production of the turbine to the annual energy production of the wind plant.
   -  :code:`fixed_charge_rate`: Float defining the fixed charge rate for the project.
   -  :code:`bos_per_kW`: Float defining the balance of station costs expressed in $/kW.
   -  :code:`opex_per_kW`: Float defining the operational expenditures expressed in $/kW.
   -  :code:`turbine_number`: Integer specifying the number of turbines in the wind park.