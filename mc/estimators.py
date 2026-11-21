import numpy as np
from scipy.stats import norm

def mc_estimate(samples, confidence=0.95):
    """Turn Monte Carlo samples into an estimate with an error bar
    
    Args:
        samples: array of iid sample values f(X_1), ..., f(X_n)
        confidence: confidence level for the interval, eg 0.95
        
    Returns:
        dict with keys: mean, s, se, ci_low, ci_high, n
    """
    x = np.asarray(samples, dtype=float) #turn arrays into numpy arrays
    n = len(x) #how many samples

    mean = np.mean(x) #mean of the samples
    s = np.std(x, ddof=1) #sample standard deviation
    se = s/np.sqrt(n) #standard error of the mean

    z = norm.ppf(0.5 + confidence/2) #z-score for the confidence level
    ci_low = mean - z*se #lower bound of the confidence interval
    ci_high = mean + z*se #upper bound of the confidence interval

    return dict(mean=float(mean), s=float(s), se=float(se), ci_low=float(ci_low), ci_high=float(ci_high), n=int(n))