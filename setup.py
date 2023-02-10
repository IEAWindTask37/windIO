import setuptools

metadata = dict(
    name="windIO",
    url='https://github.com/IEAWindTask37/windIO',
    version="1.0",
    description="Frameworks defining the inputs and outputs for systems engineering MDAO of wind turbine and plants.",
    author="IEA Wind Task 37",
    packages=setuptools.find_packages(exclude=["test", "examples"]),
    python_requires=">=3.7",
    zip_safe=True,
    install_requires=['jsonschema', 'numpy', 'pyyaml', 'pytest', 'xarray']
    )

setuptools.setup(**metadata)