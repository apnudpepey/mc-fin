import numpy as np

from mc.analytic import bs_call
from mc.estimators import mc_estimate
from mc.paths import gbm_terminal, gbm_paths
from mc.payoffs import call_payoff, asian_call_payoff

def test_mc_call_matches_black_scholes():
    S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1
    rng = np.random.default_rng(0)
    S_T = gbm_terminal(S0, r, sigma, T, 200_000, rng)
    result = mc_estimate(np.exp(-r * T) * call_payoff(S_T, K))
    exact = bs_call(S0, K, r, sigma, T)
    assert abs(result["mean"] - exact) < 3 * result["se"]

def test_asian_with_one_date_matches_black_scholes():
    # With m = 1 the average is just S(T), so the Asian call is a European call
    S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1
    rng = np.random.default_rng(0)

    paths = gbm_paths(S0, r, sigma, T, 1, 200_000, rng)          # m = 1
    payoffs = np.exp(-r * T) * asian_call_payoff(paths, K)            # discounted Asian payoffs
    result = mc_estimate(payoffs)
    exact = bs_call(S0, K, r, sigma, T)
    assert abs(result["mean"] - exact) < 3 * result["se"]