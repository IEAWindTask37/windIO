Turbine
------------

The wind turbine ontology, which is currently implemented in YAML and supported by a JSON schema, is developed defining nine top-level entries.

.. literalinclude:: ../../test/top_level.yaml
    :start-after: # Top level entries of the IEA Wind Task 37 wind turbine ontology
    :end-before: # EOF


These fields consist of :code:`name`, the unique identifier of the wind turbine model, :code:`description`, a text field to describe the wind turbine, the changes to previous versions, etc, :code:`components`, a nested dictionary structure of components composing the wind turbine assembly, :code:`airfoils`, a list of airfoils, each being a dictionary that can be referenced at the component level, :code:`materials`, a list of materials, each being a dictionary that can be referenced at the component level, :code:`assembly`, a dictionary reporting the macro parameters of the wind turbine assembly, :code:`control`, a dictionary reporting the data describing the wind turbine control, :code:`environment`, a dictionary reporting the data describing the environment where the wind turbine operates, :code:`costs`, a dictionary reporting the main inputs for a levelized cost of energy analysis.

In the pages below a detailed explanation of the sub-fields of each entry is provided (:code:`name` and :code:`description` are not listed given their simplicity).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   components
   airfoils
   materials
   assembly
   control
   environment
   costs