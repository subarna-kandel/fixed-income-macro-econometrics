"""Macroeconomic time series and sovereign yield data utilities."""

import numpy as np
import pandas as pd


def generate_collinear_data(n=200, rho=0.85, random_seed=42):
    """Generate synthetic predictors with controlled multicollinearity."""
    rng = np.random.default_rng(random_seed)
    X = rng.normal(0.0, 1.0, n)
    U = rng.normal(0.0, 1.0, n)
    Z = rho * X + np.sqrt(max(0.0, 1.0 - rho**2)) * U
    epsilon = rng.normal(0.0, 0.5, n)
    y = 2.0 * X + 1.5 * Z + epsilon
    return pd.DataFrame({'X': X, 'Z': Z}), y
