import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path("figures").mkdir(exist_ok=True)

from mc.analytic import bs_call
from mc.estimators import mc_estimate
from mc.paths import gbm_terminal
from mc.payoffs import call_payoff

S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1
exact = bs_call(S0, K, r, sigma, T)
rng = np.random.default_rng(42)

ns = [100, 1_000, 10_000, 100_000, 1_000_000]
ses = []
errors = []

for n in ns:
    S_T = gbm_terminal(S0, r, sigma, T, n, rng)  # simulate n stock prices
    result = mc_estimate(np.exp(-r * T) * call_payoff(S_T, K))  # mc_estimate of discounted payoffs
    ses.append(result["se"])
    errors.append(abs(result["mean"] - exact))  # |MC price - exact|

# fit the slope on log-log scale
slope, intercept = np.polyfit(np.log(ns), np.log(ses), 1)
print("fitted slope of SE:", slope)             # should be close to -0.5

# plot
plt.figure(figsize=(6, 4))
plt.loglog(ns, ses, "o-", label="standard error")
plt.loglog(ns, errors, "s--", label="actual error |MC - BS|")
ref = ses[-1] * (np.array(ns) / ns[-1]) ** (-0.5)     # reference line: slope -1/2
plt.loglog(ns, ref, ":", color="gray", label="slope -1/2")
plt.xlabel("number of samples n")
plt.ylabel("error")
plt.title("Monte Carlo convergence: European call")
plt.legend()
plt.tight_layout()
plt.savefig("figures/convergence.png", dpi=150)
plt.show()