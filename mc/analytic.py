import numpy as np
from scipy.stats import norm

def bs_call(S0, K, r, sigma, T):
    """Black-Scholes formula for a European call option
    
    Args:
        S0: initial stock price
        K: strike price
        r: risk-free interest rate
        sigma: volatility of the underlying stock
        T: time to maturity in years
    
    Returns:
        call option price
    """
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    call_price = S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return call_price