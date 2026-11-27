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

def asian_call_payoff(paths, K):
    """Payoff of an arithmetic-average Asian call

    Args:
        paths: array of shape (n, m), one simulated path per row.
        K: strike price.

    Returns:
        Array of n payoffs, max(average of each row - K, 0).
    """
    S_bar = paths.mean(axis=1)     # average along each row
    return call_payoff(S_bar, K)   # reuse an existing function

def lookback_payoff(paths, S0):
    """Floating-strike lookback: max price over the path (including S0) minus the final price

    Args:
        paths: array (n, m) of simulated prices.
        S0: starting price (counts as a possible maximum).

    Returns:
        Array of n payoffs.
    """
    path_max = np.maximum(paths.max(axis=1), S0)   # highest price on each path, at least S0
    S_T = paths[:, -1]
    return path_max - S_T