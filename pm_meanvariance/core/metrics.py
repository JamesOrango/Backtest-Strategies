import matplotlib.pyplot as plt

def print_summary(returns_pf, initial_value=1_000_000):
    """
    Imprime valor final e plota evolução do portfólio.
    """
    # valor acumulado
    nav = (1 + returns_pf).cumprod() * initial_value
    final_val = nav.iloc[-1]
    print(f"Final Portfolio Value: ${final_val:,.2f}")

    # plot
    plt.figure(figsize=(10, 5))
    plt.plot(nav.index, nav.values)
    plt.title("Portfolio NAV Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
