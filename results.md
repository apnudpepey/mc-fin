# Results

All prices use S0 = 100, K = 100, r = 5%, σ = 20%, T = 1 unless stated.

| Method | Option | n | Price | SE | Benchmark | Variance ratio | Time (s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plain MC | European call | 100,000 | 10.383 | 0.047 | BS 10.451 (inside 95% CI) | 1 | |
| Plain MC | Asian call, 12 monthly dates | 100,000 | 6.198 | 0.027 | No closed form; m = 1 matches BS | 1 | |
| Plain MC | Lookback, m = 4 / 12 / 52 / 252 | 100,000 | 8.84 / 10.86 / 12.56 / 13.52 | 0.03 | Continuous 14.29; bias −5.46 → −0.77 (≈ 1/√m) | 1 | |