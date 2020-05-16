Materials
------------

windIO defines a material database, which consists of a list of entries each marked by a dash. 

.. literalinclude:: ../../test/turbine_example.yaml
    :start-after: # Materials
    :end-before: # Assembly

Each material can be described with the following mechanical properties.
    - :code:`name`: String identifying the name of the material
    - :code:`description`: Optional string to describe the material
    - :code:`source`: Optional string to describe the origin of the material, for example referencing a report or a paper
    - :code:`orth`: Boolean to specify whether a material is isotropic (0) or orthotropic (1). This determines whether some of the fields below are specified as a float or an array of floats.
    - :code:`rho`: Float specifying the density of the material. For composites, this is the density of the laminate once cured. The unit of measure is kg/m3.
    - :code:`E`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the stiffness modulus. For orthotropic materials, it consists of an array with E11, E22, and E33 (see below about the reference system). The unit of measure is Pa.
    - :code:`G`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the shear stiffness modulus. For orthotropic materials, it consists of an array with G12, G13, and G23. The unit of measure is Pa.
    - :code:`nu`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the Poisson ratio. For orthotropic materials, it consists of an array with nu12, nu13, and nu23. The unit of measure is -.
    - :code:`Xt`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the ultimate tensile strength. For orthotropic materials, it consists of an array with Xt11, Xt13, and Xt23. The unit of measure is Pa.
    - :code:`Xc`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the ultimate compressive strength. For orthotropic materials, it consists of an array with Xc11, Xc13, and Xc23. The unit of measure is Pa and values are defined positive.
    - :code:`Xy`: Float (:code:`orth=0`) specifying the ultimate yield strength. The unit of measure is Pa.
    - :code:`S`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the ultimate shear strength. For orthotropic materials, it consists of an array with S12, S13, and S23. The unit of measure is Pa and values are defined positive.
    - :code:`alpha`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the thermal coefficient of expansion. For orthotropic materials, it consists of an array with alpha11, alpha13, and alpha23. The unit of measure is 1/K and values are defined positive.
    - :code:`GIc`: Float describing the mode 1 critical energy-release rate. It is used by NuMAD from Sandia National Laboratories. The unit of measure is J/m2.
    - :code:`GIIc`: Float describing the mode 2 critical energy-release rate. It is used by NuMAD from Sandia National Laboratories. The unit of measure is J/m2.
    - :code:`alp0`: Float describing the fracture angle under pure transverse compression. It is used by NuMAD from Sandia National Laboratories. The unit of measure is radians.
    - :code:`fvf`: Float describing the fiber volume fraction of a composite material. The minimum values is 0 (only matrix), the maximum value is 1 (only fibers).
    - :code:`fwf`: Float describing the fiber weight fraction of a composite material. The minimum values is 0 (only matrix), the maximum value is 1 (only fibers).
    - :code:`ply_t`: Float describing the ply thickness of a composite material. The unit of measure is m. The actual laminate thickness is defined in the fields :code:`components`.
    - :code:`unit_cost`: Float describing the unit cost of the material. The unit of measure is $/kg. For composites, this is the unit cost of the dry fabric.
    - :code:`fiber_density`: Float describing the density of the fibers of a composite material. The unit of measure is kg/m3. Standard glass fiber has a fiber density of approximately 2600 kg/m3, while standard carbon fiber has a fiber density of approximately 1800 kg/m3.
    - :code:`A`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the fatigue S/N curve fitting parameter S=A*N^(-1/m).
    - :code:`m`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the fatigue S/N curve fitting parameter S=A*N^(-1/m).
    - :code:`R`: Float (:code:`orth=0`) or array of three floats (:code:`orth=1`) specifying the fatigue stress ratio.
    - :code:`area_density_dry`: Float describing the aerial density of a fabric of a composite material. The unit of measure is kg/m2.
    - :code:`waste`: Float describing the fraction of material that ends up wasted during manufacturing. This quantity is used in the NREL blade cost model https://www.nrel.gov/docs/fy19osti/73585.pdf. The unit of measure is -.
    - :code:`roll_mass`: Float describing the mass of a roll of fabric. This quantity is used in the NREL blade cost model https://www.nrel.gov/docs/fy19osti/73585.pdf. The unit of measure is kg.
    - :code:`component_id`: Integer used by the NREL blade cost model https://www.nrel.gov/docs/fy19osti/73585.pdf to define the manufacturing process behind a laminate. 0 - coating, 1 - sandwich filler , 2 - shell skin, 3 - shear webs, 4 - spar caps, 5 - TE reinf.

The schema enforces that the fields :code:`name`, :code:`orth`, :code:`rho`, :code:`E`, and :code:`nu` are specified.

For composites, direction 1 is aligned with the main fiber direction, direction 2 is in the plane transverse to the fibers, and direction 3 is perspendicular to the laminate plane. 


