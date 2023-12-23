import matplotlib.pyplot as plt
import numpy as np
import argparse

from os.path import exists


class Star:
    def __init__(self, file_name: str) -> None:
        if not exists(file_name):
            raise FileNotFoundError(f"Nie odnaleziono pliku {file_name}!")

        if not file_name.endswith(".dat"):
            raise Exception(f"Plik {file_name} nie posiada rozszerzenia .dat!")

        self._file_name = file_name

    def _get_data(self) -> list[list[float]]:
        time = np.array([])
        amplitude = np.array([])

        with open(self._file_name, "r") as of:
            lines = np.array([x.strip().split()[:2] for x in of.readlines()])
            for line in lines:
                time = np.append(time, float(line[0]))
                amplitude = np.append(amplitude, float(line[1]))

        return np.array([time, amplitude / 100])

    def show_plot(self) -> None:
        time = self._get_data()[0]
        ampl = self._get_data()[1]

        plt.figure(figsize=(20, 7))
        plt.scatter(time, ampl, color="black")
        plt.minorticks_on()
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()

    @property
    def file_name(self) -> str:
        return self._file_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    star = Star(args.file)
    star.show_plot()
