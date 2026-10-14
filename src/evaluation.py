"""Cook's distance outlier detection, AIC/BIC, and regression diagnostics."""

import numpy as np


def cook_distance(X, y, beta_hat):
    """Calculate Cook's distance for linear regression outlier identification."""
    n, p = X.shape
    residuals = y - X @ beta_hat
    leverage = np.diag(X @ np.linalg.pinv(X.T @ X) @ X.T)
    mse = np.sum(residuals ** 2) / max(n - p, 1)
    d = (residuals ** 2 * leverage) / (p * mse * (1.0 - leverage) ** 2 + 1e-12)
    return d


def information_criteria(y_true, y_pred, k_params):
    """Compute Akaike (AIC) and Bayesian (BIC) Information Criteria."""
    n = len(y_true)
    rss = np.sum((y_true - y_pred) ** 2)
    aic = n * np.log(rss / n) + 2.0 * k_params
    bic = n * np.log(rss / n) + np.log(n) * k_params
    return {'AIC': aic, 'BIC': bic}
