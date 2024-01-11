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


