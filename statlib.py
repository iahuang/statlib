"""
statlib - A collection of useful computation functions for STA247 at the University of Toronto.

By Ian Huang; released under the MIT license.
"""

from typing import Callable, Optional
import math


def dist_pois(l: float) -> Callable[[int], float]:
    """
    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Pois(l)`
    """

    return lambda k: math.pow(l, k) * math.pow(math.e, -l) / math.factorial(k)


def dist_binom(n: int, p: float) -> Callable[[int], float]:
    """
    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Binom(n, p)`
    """

    assert 0 <= p <= 1

    return lambda k: math.comb(n, k) * math.pow(p, k) * math.pow(1 - p, n - k)


def dist_geom(p: float) -> Callable[[int], float]:
    """
    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Geom(p)`
    """

    assert 0 <= p <= 1

    return lambda k: math.pow(1 - p, k - 1) * p


def dist_nb(r: int, p: float) -> Callable[[int], float]:
    """
    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~NB(r, p)`

    The definition of the negative binomial distribution used here is
    ```latex
    P(X=k)=\\binom{k-1}{r-1}p^r(1-p)^{k-r}
    ```
    i.e. `k` represents the number of trials before the `r`th success, with a probability `p`
    of success.
    """

    assert r >= 0

    return lambda k: math.comb(k - 1, r - 1) * math.pow(p, r) * math.pow(1 - p, k - r)


def dist_hypergeom(r: int, N: int, n: int) -> Callable[[int], float]:
    """
    Return a probability function `P` that returns the value of `P(X=k)`
    where `X` is described by a hypergeometric distribution with parameters `r`, `N`, and `n`
    defined by

    ```latex
    P(X=k)=\\frac{]\binom{r}{k}\\binom{N-r}{n-k}}{\\binom{N}{n}}
    ```

    where `N` is the population size, `r` is the number of successes in the population,
    `n` is the sample size, and `k` is the number of sample successes.
    """

    assert max(0, n - (N - r)) <= min(n, r)

    return lambda k: (math.comb(r, k) * math.comb(N - r, n - k)) / math.comb(N, n)


def approx_integral(f: Callable[[float], float], a: float, b: float, res=1000) -> float:
    """
    Approximate the value of the integral of `f(x)` with respect to `x`, evaluated
    from `a` to `b`, where `dx` is approximated as `(b-a)/res`.
    """

    if b < a:
        return approx_integral(f, b, a, res)

    def safe_eval_f(x: float) -> float:
        try:
            return f(x)
        except ValueError:
            return 0.0

    A = 0

    x = a
    dx = (b - a) / res
    last = safe_eval_f(a)

    while x < b:

        current = safe_eval_f(x + dx)
        dA = 0.5 * dx * (last + current)
        A += dA
        x += dx
        last = current

    return A


def expected_val_continuous(
    pdf: Callable[[float], float], g: Optional[Callable[[float], float]], inf=20, dx=0.01
) -> float:
    """
    Approximate the expected value of a continuous random variable with provided
    probability density function `pdf` by integrating from `-inf` to `inf`.

    Optionally, compute the expected value of g(X)
    """

    res = round(2 * inf / dx)

    if g:
        return approx_integral(f=lambda x: g(x) * pdf(x), a=-inf, b=inf, res=res)

    return approx_integral(f=lambda x: x * pdf(x), a=-inf, b=inf, res=res)


def variance_continuous(pdf: Callable[[float], float], inf=20, dx=0.01) -> float:
    """
    Approximate the variance of a continuous random variable with provided
    probability density function `pdf` by integrating from `-inf` to `inf` to
    approximating the expected value.
    """
    
    mu = expected_val_continuous(pdf, None, inf, dx)
    return expected_val_continuous(pdf, lambda x: x * x, inf, dx) - mu * mu


def Gamma(z: float) -> float:
    """
    Approximate the value of `G(z)`, where `G` is the gamma function.

    Algorithm from:
    ```text
    Yang ZH, Tian JF. An accurate approximation formula for gamma function.
    J Inequal Appl. 2018;2018(1):56. doi:10.1186/s13660-018-1646-6
    ```
    """

    if math.isclose(z % 1, 0):
        return math.factorial(round(z) - 1)

    z -= 1

    return (
        math.sqrt(2 * math.pi * z)
        * math.pow(z / math.e, z)
        * math.pow(z * math.sinh(1 / z), z / 2)
        * math.exp(7 / (324 * z * z * z * (35 * z * z + 33)))
    )


def dist_exp(l: float) -> Callable[[float], float]:
    """
    Return the probability density function of a random variable X
    described by an exponential distribution with parameter `l`
    """

    return lambda x: l * math.pow(math.e, -l * x) if x >= 0 else 0


def dist_gamma(alpha: float, beta: float) -> Callable[[float], float]:
    """
    Return the probability density function of a random variable X
    described by a gamma distribution with shape parameter `alpha` and scale parameter `beta`.
    """

    denom = Gamma(alpha) * math.pow(beta, alpha)

    return lambda x: (math.pow(x, alpha - 1) * math.pow(math.e, -x / beta)) / denom if x > 0 else 0
