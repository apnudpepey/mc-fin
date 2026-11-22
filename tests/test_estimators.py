import numpy as np
import pytest

from mc.estimators import mc_estimate

def test_known_values():
    result = mc_estimate([1.0, 2.0, 3.0, 4.0])
    assert result["mean"] == pytest.approx(2.5)
    assert result["s"] == pytest.approx(np.sqrt(5/3))
    assert result["se"] == pytest.approx(np.sqrt(5/3) / 2)
    assert result["n"] == 4

def test_interval_is_symmetric():
    result = mc_estimate([1.0, 2.0, 3.0, 4.0])
    lower_bound = result["mean"] - result["ci_low"]
    upper_bound = result["ci_high"] - result["mean"]
    assert lower_bound == pytest.approx(upper_bound)

def test_se_halves_when_n_quadruples():
    rng = np.random.default_rng(seed=42)
    se_small = mc_estimate(rng.normal(size=10000))["se"]
    se_large = mc_estimate(rng.normal(size=40000))["se"]
    assert se_large == pytest.approx(se_small / 2, rel=0.05)

@pytest.mark.parametrize("bad", [[], [1.0], [1.0, np.nan]])
def test_rejects_bad_samples(bad):
    with pytest.raises(ValueError):
        mc_estimate(bad)