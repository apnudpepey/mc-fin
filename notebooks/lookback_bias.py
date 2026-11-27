import numpy as np

from mc.estimators import mc_estimate
from mc.paths import gbm_paths
from mc.payoffs import lookback_payoff

S0, r, sigma, T = 100, 0.05, 0.2, 1
n = 100_000
TRUE_CONTINUOUS = 14.291   # exact price if you could watch every instant (closed-form lookback formula)

for m in [4, 12, 52, 252]:
    rng = np.random.default_rng(7)
    paths = gbm_paths(S0, r, sigma, T, m, n, rng)
    result = mc_estimate(np.exp(-r * T) * lookback_payoff(paths, S0))
    bias = result["mean"] - TRUE_CONTINUOUS
    print(f"m={m:>3}: price={result['mean']:.3f}  SE={result['se']:.3f}  "
          f"bias={bias:+.3f}  bias/SE={bias / result['se']:+.0f}")