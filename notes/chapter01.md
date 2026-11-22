# Chapter 1.1: Principles of Monte Carlo

**Question this section answers:** How can random sampling compute an expectation (integral)? How accurate?
## Method:
Write the quantity as average $\mathbb{E}[f(U)]$, and estimate by averaging f over n random samples. Sample's SD gives a SE, and mean $\pm$ 1.96 SE is 95% confidence interval.
## Key formula(s)
Monte Carlo estimate:
$$
\hat\alpha_n = \frac{1}{n}\sum_{i=1}^{n} f(U_i)
$$

Sample standard deviation:
$$
s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}\big(f(U_i) - \hat\alpha_n\big)^2}
$$

Standard error and 95% confidence interval:
$$
\text{SE} = \frac{s}{\sqrt{n}}, \qquad \hat\alpha_n \pm 1.96\,\text{SE}
$$
## Limitations:
- Halving the error needs 4 times the sample size
- In 1 dimension, grid method is faster. Monte Carlo only wins from dimensions > 4
- Assume independent samples
## My numbers
| Problem | n | Estimate | SE | True value | Within 2 SE? |
| --- | --- | --- | --- | --- | --- |
| π (darts) | 10,000 | 3.1488 | 0.0164 | 3.14159 | Yes |
| $\int_0^1 e^x\,dx$ | 10,000 | 1.7223 | 0.0049 | 1.71828 | Yes |

Same $n$, but $e^x$ is ~3× more accurate: it varies less, so $s$ is smaller.

