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