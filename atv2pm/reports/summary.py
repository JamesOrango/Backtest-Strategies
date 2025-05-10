import matplotlib.pyplot as plt

def plot_performance(returns):
    cumulative = (1 + returns).cumprod()
    cumulative.plot(title="Walk-Forward Portfolio Value", figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()