import numpy as np

def gbm_terminal(S0, r, sigma, T, n, rng):
    """Simulaten n terminal stock prices using Geometric Brownian Motion
    
    Args:
        S0: initial stock price
        r: risk-free interest rate
        sigma: volatility of the stock
        T: time to maturity in years
        n_paths: number of simulated paths
        rng: optional random number generator 
    
    Returns:
        array of simulated terminal stock prices
    """
    Z = rng.standard_normal(n)
    drift = (r - 0.5 * sigma**2)*T
    ST = S0 * np.exp(drift + sigma * np.sqrt(T) * Z)
    return ST

def gbm_paths(S0, r, sigma, T, m, n, rng):
    """Simulate n GBM paths at m equally spaced dates up to T 

    New args:
        m: number of dates (e.g. 12 for monthly).
        n: number of paths.

    Returns:
        Array of shape (n, m): row i is path i, column j is the price at date j+1.
    """
    dt = T / m                               # length of each step
    Z = rng.standard_normal((n, m))          # n x m grid of independent normals
    steps = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
    log_paths = np.cumsum(steps, axis=1)     # running total across each row
    return S0 * np.exp(log_paths)            # S0 * exp(...)