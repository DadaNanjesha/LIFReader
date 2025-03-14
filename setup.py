import setuptools
from os import path, find_packages

# Get the long description from README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LIFReader",
    version="1.0.0",
    author="Dada Nanjesha",
    description="A tool for parsing and visualizing AGV layouts from LIF files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DadaNanjesha/LIFReader",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "networkx",
        "matplotlib",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "lifreader=main:main",  # If you want a command-line entry point
        ],
    },
)
