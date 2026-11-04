#!/usr/bin/env python3
"""Binomial distribution"""


class Binomial:
    """Represents a binomial distribution: the number of successes in n
    independent trials, each with probability p of success."""

    def __init__(self, data=None, n=1, p=0.5):
        """Sets n and p, estimated from data if given"""

        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )

            self.n = int(n)
            self.p = float(p)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # For a binomial: mean = n * p and variance = n * p * (1 - p)
            mean = sum(data) / len(data)
            variance = sum(
                (x - mean) ** 2 for x in data
            ) / len(data)

            # variance / mean = 1 - p, so first estimate p ...
            p = 1 - variance / mean
            # ... use it to get n, which must be a whole number of trials
            n = round(mean / p)

            # recompute p from the rounded n so that n * p == mean
            self.n = n
            self.p = mean / n

    def pmf(self, k):
        """PMF for k successes: C(n, k) * p^k * (1 - p)^(n - k)"""
        # k must be a whole number of successes
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        # binomial coefficient C(n, k) = n! / ((n - k)! * k!)
        cnk = self.factorial(self.n) \
            / (self.factorial(self.n - k) * self.factorial(k))

        return cnk * self.p ** k * (1 - self.p) ** (self.n - k)

    def cdf(self, k):
        """CDF for k successes: the sum of the PMF from 0 to k"""
        # k must be a whole number of successes
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        result = 0

        # add up P(i) for i = 0, 1, ..., k
        for i in range(0, k+1):
            cnk = self.factorial(self.n) \
                / (self.factorial(self.n - i) * self.factorial(i))

            result += cnk * self.p ** i * (1 - self.p) ** (self.n - i)

        return result

    def factorial(self, n):
        """Returns n!, computed by hand"""
        result = 1
        for i in range(1, n+1):
            result *= i

        return result
