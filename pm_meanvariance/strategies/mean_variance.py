import numpy as np
import pandas as pd

def mean_variance_optimizer(returns):
    mu = returns.mean()
    cov = returns.cov()
    inv_cov = np.linalg.pinv(cov)
    ones = np.ones(len(mu))
    weights = inv_cov @ mu
    weights = weights / np.sum(weights)
    return pd.Series(weights, index=mu.index)