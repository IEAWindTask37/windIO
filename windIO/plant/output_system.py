%YAML 1.2
---
$schema: "http://json-schema.org/draft-07/schema#"
type: object
properties:
  name:
    type: string
  FLOW_simulation_config:
    type: object
    properties:
      tool:
        type: string
      wake_model:
        type: string
      wind_energy_system: !include wind_energy_system.yaml
  FLOW_simulation_outputs:
    type: object
    properties:
      AEP:
        type: number
      AEP_per_turbine:
        type: array
        items:
          type: number
      computed_percentiles:
        type: array
        items:
          type: integer
      power_output_variables:
        type: array
        items:
          type: string
      power_percentiles:
        type: array
        items:
          type: number
      statistical_description:
        type: string
      wind_output_file:
        type: string
      wind_output_variables:
        type: array
        items:
          type: string
required:
  - name
  - FLOW_simulation_config
  - FLOW_simulation_outputs

