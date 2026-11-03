# Probability

Probability distributions written from scratch in Python 3, with no external
libraries. Each distribution is a class that can be built in two ways: from
its parameters, or estimated from a list of sample values. It then exposes the
usual functions: the **PMF/PDF** (how likely one value is) and the **CDF**
(how likely a value up to x is).

| File | Class | Distribution | Tasks | Status |
| --- | --- | --- | --- | --- |
| `poisson.py` | `Poisson` | Poisson (discrete) | 0–2 | done |
| `exponential.py` | `Exponential` | Exponential (continuous) | 3–5 | done |
| `normal.py` | `Normal` | Normal / Gaussian (continuous) | 6–9 | done |
| `binomial.py` | `Binomial` | Binomial (discrete) | 10–12 | not started |

---

## Quick start

```bash
pip install numpy      # only the main files use it, to generate sample data
cd math/probability
./0-main.py            # every N-main.py runs the matching task
```

Or use a class straight from Python:

```python
Normal = __import__('normal').Normal
n = Normal(mean=70, stddev=10)
print(n.cdf(90))
```

---

## Poisson distribution — `poisson.py`

Counts how many times an event happens in a fixed interval, when events occur
independently at a constant average rate. It is described by one value,
**lambtha** (λ), the expected number of events in the interval.

```
 P(k)
  │   ▂▅▇█▇▅▃▂▁
  │ ▂▅█████████▅▃▂▁
  └──┴──┴──┴──┴──┴──┴──┴──▶ k  (number of events)
     0  1  2  3  4  5  6  7
```

### 0. Initialize Poisson — `Poisson(data=None, lambtha=1.)`

- Without `data`: uses the given `lambtha` (stored as a float).
  Raises `ValueError("lambtha must be a positive value")` if `lambtha <= 0`.
- With `data`: estimates `lambtha` from the sample.
  - `TypeError("data must be a list")` if `data` is not a list.
  - `ValueError("data must contain multiple values")` if it has fewer than
    two values.
  - `lambtha = sum(data) / n` — the mean of the data.

### 1. Poisson PMF — `pmf(k)`

The probability of exactly `k` events. `k` is turned into an integer first,
and the result is `0` if `k < 0`.

```
 P(k) = λ^k · e^(-λ) / k!
```

### 2. Poisson CDF — `cdf(k)`

The probability of `k` events or fewer, the sum of the PMF from 0 to `k`.
`k` is turned into an integer first, and the result is `0` if `k < 0`.

```
 F(k) = e^(-λ) · Σ (i = 0 to k)  λ^i / i!
```

### Expected output

| Main file | Output |
| --- | --- |
| `0-main.py` | `Lambtha: 4.84`<br>`Lambtha: 5.0` |
| `1-main.py` | `P(9): 0.03175849616802446`<br>`P(9): 0.036265577412911795` |
| `2-main.py` | `F(9): 0.9736102067423525`<br>`F(9): 0.968171942620861` |

The first line of each pair comes from 100 random samples
(`np.random.poisson(5., 100)` with seed 0), the second from
`Poisson(lambtha=5)`.

---

## Exponential distribution — `exponential.py`

Measures the time you wait until the next event, when events happen
independently at a constant average rate. It is described by one value,
**lambtha** (λ), the number of events per unit of time. The mean waiting time
is `1 / λ`.

```
 f(x)
  │█
  │██▇
  │████▆▅
  │███████▆▅▄▃▂▂▁
  └──────────────────▶ x  (time)
```

### 3. Initialize Exponential — `Exponential(data=None, lambtha=1.)`

- Without `data`: uses the given `lambtha` as it is.
  Raises `ValueError("lambtha must be a positive value")` if `lambtha <= 0`.
- With `data`: estimates `lambtha` from the sample.
  - `TypeError("data must be a list")` if `data` is not a list.
  - `ValueError("data must contain multiple values")` if it has fewer than
    two values.
  - `lambtha = n / sum(data)` — the inverse of the mean of the data.

### 4. Exponential PDF — `pdf(x)`

The density of waiting exactly `x` time units. `x` is a time, so the result is
`0` if `x < 0`.

```
 f(x) = λ · e^(-λx)
```

### 5. Exponential CDF — `cdf(x)`

The probability of waiting `x` time units or less. The result is `0` if
`x < 0`.

```
 F(x) = 1 - e^(-λx)
```

### Expected output

| Main file | Output |
| --- | --- |
| `3-main.py` | `Lambtha: 2.177111473090695`<br>`Lambtha: 2` |
| `4-main.py` | `f(1): 0.24681591903431552`<br>`f(1): 0.2706705664650693` |
| `5-main.py` | `F(1): 0.8866314738197911`<br>`F(1): 0.8646647167674654` |

The first line of each pair comes from 100 random samples
(`np.random.exponential(0.5, 100)` with seed 0), the second from
`Exponential(lambtha=2)`.

---

## Normal distribution — `normal.py`

The bell curve, described by its **mean** (μ, the centre) and its
**standard deviation** (σ, the spread).

```
                 ▁▃▅▇█▇▅▃▁
              ▁▃▅█████████▅▃▁
         ▁▂▃▅▇███████████████▇▅▃▂▁
 ───────┼───────┼───────┼───────┼───────┼──
      μ-2σ    μ-σ       μ      μ+σ    μ+2σ
```

### 6. Initialize Normal — `Normal(data=None, mean=0., stddev=1.)`

- Without `data`: uses the given `mean` and `stddev` (stored as floats).
  Raises `ValueError("stddev must be a positive value")` if `stddev <= 0`.
- With `data`: estimates both values from the sample.
  - `TypeError("data must be a list")` if `data` is not a list.
  - `ValueError("data must contain multiple values")` if it has fewer than
    two values.
  - `mean = sum(data) / n`
  - `stddev = sqrt(sum((x - mean)²) / n)` — the **population** standard
    deviation (divided by `n`, not `n - 1`).

### 7. Normalize Normal — `z_score(x)` and `x_value(z)`

The z-score says how many standard deviations a value is from the mean. The
two methods are the inverse of each other.

```
 z_score(x) = (x - μ) / σ
 x_value(z) = z · σ + μ
```

### 8. Normal PDF — `pdf(x)`

```
           1            -z² / 2
 f(x) = ─────────── · e            with z = z_score(x)
         σ · √(2π)
```

### 9. Normal CDF — `cdf(x)`

The probability that a value is less than or equal to `x`:

```
 F(x) = ½ · (1 + erf(t))           with t = (x - μ) / (σ · √2)
```

`erf` has no closed form, so it is approximated with the first five terms of
its Maclaurin series:

```
 erf(t) ≈ 2/√π · (t - t³/3 + t⁵/10 - t⁷/42 + t⁹/216)
```

The approximation is very good close to the mean and drifts as `|t|` grows,
which is why the results differ slightly from SciPy's.

### Expected output

| Main file | Output |
| --- | --- |
| `6-main.py` | `Mean: 70.59808015534485 , Stddev: 10.078822447165797`<br>`Mean: 70.0 , Stddev: 10.0` |
| `7-main.py` | `Z(90): 1.9250185174272068` / `X(2): 90.75572504967644`<br>`Z(90): 2.0` / `X(2): 90.0` |
| `8-main.py` | `PSI(90): 0.006206096804434349`<br>`PSI(90): 0.005399096651147344` |
| `9-main.py` | `PHI(90): 0.9829020110852376`<br>`PHI(90): 0.9922398930659416` |

The first line of each pair comes from 100 random samples
(`np.random.normal(70, 10, 100)` with seed 0), the second from
`Normal(mean=70, stddev=10)`.

---

## Requirements and style

- Python 3; the distribution classes compute everything by hand, and
  constants such as π (`3.1415926536`) and e (`2.7182818285`) are written
  out instead of taken from the `math` module
- NumPy is only used by the `N-main.py` files to generate test data
- Files start with `#!/usr/bin/env python3` and are executable
- Code follows `pycodestyle` (max 79 characters per line)
- Every module, class and method has a docstring
