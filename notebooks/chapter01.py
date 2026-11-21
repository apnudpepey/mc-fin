import numpy as np
from mc.estimators import mc_estimate

rng = np.random.default_rng(42)  #random number generator with a fixed seed for reproducibility
n=10000

x = rng.random(n) #10000 random numbers between 0 and 1
y = rng.random(n)
inside = (x**2 + y**2) < 1 #did it land inside the unit circle?
f = 4*inside #true is 4, false is 0 

estimate = np.mean(f)
s_f = np.std(f, ddof=1)
se = s_f/np.sqrt(n)

print("pi estimate:", estimate, "SE:", se)
print("actual error:", abs(estimate - np.pi), "within 2 SE?", abs(estimate - np.pi) < 2*se)

u = rng.random(n) 
g = np.exp(u)
true_value = np.e - 1

estimate_g = np.mean(g)
s_g = np.std(g, ddof=1)
se_g = s_g/np.sqrt(n)

print("e estimate:", estimate_g, "SE:", se_g)
print("actual error:", abs(estimate_g - true_value), "within 2 SE?", abs(estimate_g - true_value) < 2*se_g)

#test mc_estimate function
result_pi = mc_estimate(4*inside)
print(result_pi)

result_g = mc_estimate(g)
print(result_g)
