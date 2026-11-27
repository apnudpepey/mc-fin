import time
import numpy as np

from mc.estimators import mc_estimate
from mc.paths import gbm_terminal, gbm_paths
from mc.payoffs import call_payoff

S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1
rng = np.random.default_rng(42)

def price_jump(n):
    S_T = gbm_terminal(S0, r, sigma, T, n, rng)
    return np.exp(-r * T) * call_payoff(S_T, K)

def price_walk(n):
    paths = gbm_paths(S0, r, sigma, T, 252, n, rng)
    S_T = paths[:, -1]                      
    return np.exp(-r * T) * call_payoff(S_T, K)

for name, method, n in [("A: jump", price_jump, 100_000),
                        ("B: walk 252 steps", price_walk, 20_000)]:
    start = time.perf_counter()               
    payoffs = method(n)
    elapsed = time.perf_counter() - start    

    result = mc_estimate(payoffs)
    var = result["s"] ** 2                  
    tau = elapsed / n                      
    eff = var * tau                          

    print(f"{name}: price={result['mean']:.3f}  SE={result['se']:.3f}  "
          f"var/path={var:.1f}  time/path={tau:.2e}s  var*time={eff:.2e}")