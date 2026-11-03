#!/usr/bin/env python3
"""Poisson distribution"""


class Poisson:
    """Poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Sets lambtha, estimated from data if given"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")

            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.data = data
            # lambtha is the expected number of events: the mean of the data
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """PMF for k events: lambtha^k * e^-lambtha / k!"""
        # k must be a whole number of events
        k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285

        # k! computed by hand
        k_factorial = 1
        for i in range(2, k + 1):
            k_factorial *= i

        return (self.lambtha ** k) / (k_factorial * e ** self.lambtha)

    def cdf(self, k):
        """CDF for k events: the sum of the PMF from 0 up to k"""
        # k must be a whole number of events
        k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285
        result = 0
        factorial = 1

        for i in range(0, k + 1):
            # i! is built up from (i - 1)! on each pass
            factorial *= (1 if i == 0 else i)
            result += (self.lambtha ** i) / (e ** self.lambtha * factorial)

        return result
