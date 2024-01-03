import os

from stellarflow import stellarflow as sf


class TestStar:
    def setup_method(self):
        self.star = sf.Star('stars.dat')

    def teardown_method(self):
        del self.star

    def test_init_star(self):
        assert os.path.exists('stars.dat')
        assert self.star.file_name.endswith('.dat')
        assert self.star.file_name == 'stars.dat'

    def test_detrend_by_diff(self):
        time = [8, 13, 18, 14, 13, 18, 24, 20]
        detrend = []

        for dd in range(1, len(time)):
            res = time[dd] - time[dd - 1]
            detrend.append(res)

        assert detrend == [5, 5, -4, -1, 5, 6, -4]
