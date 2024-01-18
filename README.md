![Tests](https://github.com/iadyo/stellarflow/actions/workflows/python-app.yml/badge.svg)
![Ruff](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fruff%2Fmain%2Fassets%2Fbadge%2Fv2.json)
![GitHub License](https://img.shields.io/github/license/iadyo/stellarflow)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)


This Python script provides a simple tool for visualizing and detrending stellar light curves from data stored in a '.dat' file.

### Usage:

1. Ensure you have [Poetry](https://python-poetry.org/) installed on your system.

2. Clone the repository:
   ```bash
   git clone https://github.com/iadyo/stellarflow.git
   cd stellarflow
   ```

3. Install project dependencies using Poetry:

   ```bash
   poetry install --only main
   ```

### Plotting:

Generates a scatter plot of the original light curve and overlays the detrended curve

### Example Usage:

Run the script from the command line, passing the path to the target '.dat' file as a command-line argument.

   poetry run python stellarflow.py path/to/your/light_curve.dat

### Getting help:
For additional assistance and available command-line options, run the following command:
```bash
poetry run python stellarflow.py -h
```
or
```bash
poetry shell
python stellarflow.py -h
```

### Images:

![image](https://github.com/iadyo/stellarflow/assets/60442527/8a5f9be3-9271-4942-a9bb-94973f3db265)
![image](https://github.com/iadyo/stellarflow/assets/60442527/5c1156c0-3dec-4d24-ace5-920f96cf1869)
![image](https://github.com/iadyo/stellarflow/assets/60442527/7fcd8bfe-c5f9-4d7b-bf3c-abda841fd0df)



