"""Yield curve parametric models and regression estimators."""

import numpy as np


def nelson_siegel_yield(tau, beta0, beta1, beta2, tau_scale):
    """Parametric Nelson-Siegel yield function."""
    term1 = (1.0 - np.exp(-tau / tau_scale)) / (tau / tau_scale)
    term2 = term1 - np.exp(-tau / tau_scale)
    return beta0 + beta1 * term1 + beta2 * term2


def fit_nelson_siegel(maturities, market_yields):
    """Calibrate Nelson-Siegel 4-parameter curve to market yields."""
    try:
        from scipy.optimize import minimize
        def objective(params):
            b0, b1, b2, tau_s = params
            if tau_s <= 0:
                return 1e6
            fitted = nelson_siegel_yield(maturities, b0, b1, b2, tau_s)
            return np.sum((market_yields - fitted) ** 2)

        init_params = [0.08, -0.02, 0.02, 3.0]
        res = minimize(objective, init_params, bounds=[(-0.5, 0.5), (-0.5, 0.5), (-0.5, 0.5), (0.1, 30.0)])
        return res.x
    except ImportError:
        # Direct linear least squares given a fixed grid tau_scale
        best_err = float('inf')
        best_params = None
        for tau_s in np.linspace(1.0, 5.0, 10):
            term1 = (1.0 - np.exp(-maturities / tau_s)) / (maturities / tau_s)
            term2 = term1 - np.exp(-maturities / tau_s)
            X = np.column_stack([np.ones_like(maturities), term1, term2])
            betas, residuals, _, _ = np.linalg.lstsq(X, market_yields, rcond=None)
            err = np.sum((market_yields - X @ betas)**2)
            if err < best_err:
                best_err = err
                best_params = [betas[0], betas[1], betas[2], tau_s]
        return np.array(best_params)
