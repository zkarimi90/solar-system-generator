This is a Python-package which generates a 2D solar (or rather stelar) system consisting of one sun and a user-defined number of planets orbiting around the sun in circular orbits. See the full project description [here](https://sites.google.com/view/python3-umk/projects#h.6plj5vogra3y)

The feature is not implemented yet, but eventually, the Python package will be able to determine the period of rotation of the planets around the star using Kepler's third law:

T^2 = (4 * π^2 * r^3) / (G * M)

The code is structured as follows:

solsysgen/
|----- __init__.py
|----- sun.py # Sun class
|----- planet.py # Planet class
|----- solarsystem.py # SolarSystem class
|----- utils/ # Utilities
       |----- checkpoint.py # Read/write from/to checkpoint files.


## Installation instructions
We recommend that you install the solar system generator in a conda environment. If you don't already have conda, install
[Miniconda](https://www.anaconda.com/download/success) following the [instructions](https://www.anaconda.com/docs/getting-started/miniconda/install) for your operating system. Once you have miniconda, create a new conda environment using
the [solsysgen-env.yml] file. In a terminal (or Anaconda Powershell prompt for Windows), run:

conda env create -f pysolsys-env.yml

Then, activate the conda environment:

conda activate pysolsys-env

Clone the repository and pip install:

git clone https://github.com/iubr/solar-system-generator.git
cd solar-system-generator
pip install .

## How to run

See an example Jupyter notebook in examples. You can start the notebook from a terminal (Anaconda Powershell prompt for Windows):

cd /path/to/your/solar/system/generator/examples/
conda activate pysolsys-env
jupyter-lab create_a_solar_system.ipynb

## Other useful information

This project is part of the [Python3 - 7404-FIZ-KKP](https://sites.google.com/view/python3-umk/home) course at UMK.

 
