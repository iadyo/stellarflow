from os.path import exists

import matplotlib.pyplot as plt
import numpy as np
import argparse
from sklearn.linear_model import LinearRegression


class Star:
    def __init__(self, file_name: str) -> None:
        if not exists(file_name):
            raise FileNotFoundError(f'Nie odnaleziono pliku {file_name}!')

        if not file_name.endswith('.dat'):
            raise Exception(f'Plik {file_name} nie posiada rozszerzenia .dat!')

        self._file_name = file_name

    def _get_data(self) -> np.ndarray:
        time = np.array([])
        amplitude = np.array([])

        with open(self._file_name, 'r') as of:
            lines = np.array([x.strip().split()[:2] for x in of.readlines()])
            for line in lines:
                time = np.append(time, float(line[0]))
                amplitude = np.append(amplitude, float(line[1]))

        return np.array([time, amplitude / 1000 + 1])

    def _detrend_by_diff(self, ampl) -> np.ndarray:
        detrend = np.array([ampl[dd] - ampl[dd - 1] for dd in range(1, len(ampl))])
        return detrend
    
    def _detrend_by_linear_regression(self, time) -> np.ndarray:
        X = time.reshape(-1, 1)
        y = self._get_data()[1]

        model = LinearRegression().fit(X, y)
        trend = model.predict(X)
        detrended_data = y - trend

        return detrended_data

    def show_plot(self) -> None:
        time, ampl = self._get_data()

        plt.figure(figsize=(20, 7))
        plt.scatter(time, ampl, color='black')
        # plt.plot(time[:-1], self.detrend_by_diff(ampl), ms=12, color='red')
        plt.plot(time, self._detrend_by_linear_regression(time) + 1, ms=12, color='red')
        plt.minorticks_on()
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()

    @property
    def file_name(self) -> str:
        return self._file_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    star = Star(args.file)
    star.show_plot()
