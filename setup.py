import setuptools

# Required packages to use the library
REQUIRED = [
    'jsonschema',
    'numpy',
    'pyyaml',
    'xarray',
]

# Optional packages
# To use:
#   pip install -e ".[test]"         installs testing packages in editable install
#   pip install "windIO[test]"       installs testing packages in non-editable install
EXTRAS = {
    "test": {
        'pytest',
        'py_wake',
        'topfarm',
    },
    "docs": {
        'Sphinx'
    }
}

metadata = dict(
    name="windIO",
    url='https://github.com/IEAWindTask37/windIO',
    version="1.0",
    description="Frameworks defining the inputs and outputs for systems engineering MDAO of wind turbine and plants.",
    author="IEA Wind Task 37",
    packages=setuptools.find_packages(exclude=["docs*", "examples*", "test*"]),
    python_requires=">=3.7",
    zip_safe=True,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    license="Apache-2.0",
)

setuptools.setup(**metadata)
