import pandas as pd
import numpy as np
from strategies.mean_variance import mean_variance_optimizer


def walk_forward_backtest(prices, rebalance_window=63):
    returns = prices.pct_change().dropna()
    n_periods = len(returns) // rebalance_window

    portfolio_returns = []
    dates = []

    for i in range(n_periods):
        start = i * rebalance_window
        end = start + rebalance_window

        train_returns = returns.iloc[start:end]
        test_returns = returns.iloc[end:end+rebalance_window]

        if len(test_returns) == 0:
            break

        weights = mean_variance_optimizer(train_returns)
        perf = (test_returns @ weights).values

        portfolio_returns.extend(perf)
        dates.extend(test_returns.index)

    return pd.Series(portfolio_returns, index=dates)