import numpy as np

def call_payoff(S_T, K):
    """Calculate the payoffs of a European call option
    
    Args:
        S_T: array of terminal stock prices
        K: strike price
    
    Returns:
        array of call option payoffs
    """
    return np.maximum(S_T - K, 0)