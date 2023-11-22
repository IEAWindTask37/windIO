Turbine
------------

The wind turbine ontology, which is currently implemented in YAML and supported by a JSON schema, is developed defining ten top-level entries.

:code:`name` : String
    Unique identifier of the wind turbine model
    
:code:`description` : String
    Text field to describe the wind turbine, the changes to previous versions, etc,

:code:`assembly` : Object
    Dictionary reporting the macro parameters of the wind turbine assembly
    
:code:`components` : Object
    Nested dictionary structure of components describing the wind turbine assembly
    
:code:`airfoils` : List
    List of airfoils, each being a dictionary that can be referenced at the component level
    
:code:`materials` : List
    List of materials, each being a dictionary that can be referenced at the component level
    
:code:`control` : Object
    Dictionary reporting the data describing the wind turbine control
    
:code:`environment` : Object
    Dictionary reporting the data describing the environment where the wind turbine operates
    
:code:`bos` : Object
    Dictionary reporting the main inputs for the balance of station cost analysis.

:code:`costs` : Object
    Dictionary reporting the main inputs for a levelized cost of energy analysis.

In the pages below a detailed explanation of the sub-fields of each entry is provided (:code:`name` and :code:`description` are not listed given their simplicity).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   assembly
   components
   airfoils
   materials
   control
   environment
   costs
