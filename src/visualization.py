"""Visualizations for yield curves, leverage plots, and cointegration paths."""

import matplotlib.pyplot as plt
import numpy as np


def plot_yield_curve(maturities, market_yields, fitted_curve=None, title="Sovereign Yield Curve"):
    """Plot market yields and fitted Nelson-Siegel curve."""
    plt.figure(figsize=(8, 4.5))
    plt.scatter(maturities, market_yields, color='red', label='Observed Yields')
    if fitted_curve is not None:
        grid_tau = np.linspace(min(maturities), max(maturities), 100)
        plt.plot(grid_tau, fitted_curve(grid_tau), 'b-', label='Nelson-Siegel Fit')
    plt.xlabel('Maturity (Years)')
    plt.ylabel('Yield (%)')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    return plt.gcf()
