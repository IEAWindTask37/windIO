Turbine
------------

The wind turbine ontology, which is currently implemented in YAML and supported by a JSON schema, is developed defining nine top-level entries:

name: the unique identifier of the wind turbine model

description: a text field to describe the wind turbine, the changes to previous versions, etc

components: a nested dictionary structure of components composing the wind turbine assembly

airfoils: a list of airfoils, each being a dictionary that can be referenced at the component level

materials: a list of materials, each being a dictionary that can be referenced at the component level

assembly: a dictionary reporting the macro parameters of the wind turbine assembly

control: a dictionary reporting the data describing the wind turbine control

environment: a dictionary reporting the data describing the environment where the wind turbine operates

costs: a dictionary reporting the main inputs for a levelized cost of energy analysis
