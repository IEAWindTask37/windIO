import setuptools

metadata = dict(
    name="windIO",
    url='https://github.com/IEAWindTask37/windIO',
    version="1.0",
    description="Frameworks defining the inputs and outputs for systems engineering MDAO of wind turbine and plants.",
    author="IEA Wind Task 37",
    packages=setuptools.find_packages(exclude=["docs*", "examples*", "test*"]),
    python_requires=">=3.7",
    zip_safe=True,
    install_requires=['jsonschema', 'numpy', 'pyyaml', 'pytest', 'xarray'],
    license="Apache-2.0",
)

setuptools.setup(**metadata)
