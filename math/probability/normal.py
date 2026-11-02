#!/usr/bin/env python3
"""Normal distribution"""


class Normal:
    """Normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Sets mean and stddev, from data if given"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = sum(data)/len(data)
            variance = sum((x - self.mean)**2 for x in data) / len(data)
            self.stddev = variance**0.5

    def z_score(self, x):
        """z-score of x"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """x-value of z"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """PDF at x"""
        pi = 3.1415926536
        e = 2.7182818285

        fraction = 1 / (self.stddev * (2 * pi)**0.5)
        expo = -0.5 * self.z_score(x)**2
        return fraction * e ** expo

    def cdf(self, x):
        """CDF at x"""
        pi = 3.1415926536
        t = (x - self.mean) / (self.stddev * 2 ** 0.5)
        # erf approximated with its Taylor series
        erf = (2 / pi ** 0.5) * (t - t ** 3 / 3 + t ** 5 / 10
                                 - t ** 7 / 42 + t ** 9 / 216)
        return 0.5 * (1 + erf)
