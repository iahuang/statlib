# statlib

A collection of useful computation functions for STA247 implemented in Python

## Included Functions
### `dist_pois(l)`

**Function signature:**

```
def dist_pois(l: float) -> Callable[[int], float]
```

    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Pois(l)`

### `dist_binom(n, p)`

**Function signature:**

```
def dist_binom(n: int, p: float) -> Callable[[int], float]
```

    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Binom(n, p)`

### `dist_geom(p)`

**Function signature:**

```
def dist_geom(p: float) -> Callable[[int], float]
```

    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~Geom(p)`

### `dist_nb(r, p)`

**Function signature:**

```
def dist_nb(r: int, p: float) -> Callable[[int], float]
```

    Return a probability function `P` that returns the value of `P(X=k)`
    where `X~NB(r, p)`

    The definition of the negative binomial distribution used here is
    ```latex
    P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r}
    ```
    i.e. `k` represents the number of trials before the `r`th success, with a probability `p`
    of success.

### `dist_hypergeom(r, N, n)`

**Function signature:**

```
def dist_hypergeom(r: int, N: int, n: int) -> Callable[[int], float]
```

    Return a probability function `P` that returns the value of `P(X=k)`
    where `X` is described by a hypergeometric distribution with parameters `r`, `N`, and `n`
    defined by

    ```latex
    P(X=k)=\frac{]inom{r}{k}\binom{N-r}{n-k}}{\binom{N}{n}}
    ```

    where `N` is the population size, `r` is the number of successes in the population,
    `n` is the sample size, and `k` is the number of sample successes.

### `approx_integral(f, a, b, res)`

**Function signature:**

```
def approx_integral(f: Callable[[float], float], a: float, b: float, res=1000) -> float
```

    Approximate the value of the integral of `f(x)` with respect to `x`, evaluated
    from `a` to `b`, where `dx` is approximated as `(b-a)/res`.

### `expected_val_continuous(pdf, g, inf, dx)`

**Function signature:**

```
def expected_val_continuous
```

    Approximate the expected value of a continuous random variable with provided
    probability density function `pdf` by integrating from `-inf` to `inf`.

    Optionally, compute the expected value of g(X)

### `variance_continuous(pdf, inf, dx)`

**Function signature:**

```
def variance_continuous(pdf: Callable[[float], float], inf=20, dx=0.01) -> float
```

    Approximate the variance of a continuous random variable with provided
    probability density function `pdf` by integrating from `-inf` to `inf` to
    approximating the expected value.

### `Gamma(z)`

**Function signature:**

```
def Gamma(z: float) -> float
```

    Approximate the value of `G(z)`, where `G` is the gamma function.

    Algorithm from:
    ```text
    Yang ZH, Tian JF. An accurate approximation formula for gamma function.
    J Inequal Appl. 2018;2018(1):56. doi:10.1186/s13660-018-1646-6
    ```

### `dist_exp(l)`

**Function signature:**

```
def dist_exp(l: float) -> Callable[[float], float]
```

    Return the probability density function of a random variable X
    described by an exponential distribution with parameter `l`

### `dist_gamma(alpha, beta)`

**Function signature:**

```
def dist_gamma(alpha: float, beta: float) -> Callable[[float], float]
```

    Return the probability density function of a random variable X
    described by a gamma distribution with shape parameter `alpha` and scale parameter `beta`.
