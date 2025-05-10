import backtrader as bt

def run_backtest(strategy, datafeed, start_cash=10000, stake=10, plot=False):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy)
    cerebro.adddata(datafeed)
    cerebro.broker.setcash(start_cash)
    cerebro.addsizer(bt.sizers.FixedSize, stake=stake)
    results = cerebro.run()
    if plot:
        cerebro.plot()
    return cerebro, results
