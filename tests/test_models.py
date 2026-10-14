"""Unit tests for Nelson-Siegel yield curve modeling and econometric diagnostics."""

import sys
import os
import unittest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data import generate_collinear_data
from src.features import nelson_siegel_factors
from src.models import nelson_siegel_yield, fit_nelson_siegel
from src.evaluation import cook_distance, information_criteria


class TestFixedIncomeEconometrics(unittest.TestCase):

    def test_nelson_siegel_yield_properties(self):
        tau = np.array([0.25, 1.0, 5.0, 10.0, 30.0])
        b0, b1, b2, tau_s = 0.05, -0.02, 0.01, 2.5
        y = nelson_siegel_yield(tau, b0, b1, b2, tau_s)
        self.assertEqual(len(y), len(tau))
        # As tau -> infinity, yield should approach b0
        y_long = nelson_siegel_yield(np.array([1000.0]), b0, b1, b2, tau_s)
        self.assertAlmostEqual(y_long[0], b0, delta=1e-3)

    def test_nelson_siegel_factors_loadings(self):
        tau = np.array([1.0, 5.0, 10.0])
        f1, f2, f3 = nelson_siegel_factors(tau, lambda_param=2.0)
        self.assertTrue(np.all(f1 == 1.0))  # Level is constant 1
        self.assertTrue(np.all(f2 >= 0.0))  # Slope decay
        self.assertEqual(len(f3), 3)        # Curvature humped shape

    def test_fit_nelson_siegel(self):
        maturities = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0])
        sim_yields = nelson_siegel_yield(maturities, 0.06, -0.02, 0.015, 3.0)
        fitted_params = fit_nelson_siegel(maturities, sim_yields)
        self.assertEqual(len(fitted_params), 4)
        fitted_yields = nelson_siegel_yield(maturities, *fitted_params)
        self.assertTrue(np.allclose(sim_yields, fitted_yields, atol=1e-2))

    def test_generate_collinear_data(self):
        X_df, y = generate_collinear_data(n=100, rho=0.9, random_seed=42)
        self.assertEqual(len(X_df), 100)
        corr = np.corrcoef(X_df['X'], X_df['Z'])[0, 1]
        self.assertAlmostEqual(corr, 0.9, delta=0.08)

    def test_cook_distance(self):
        X = np.ones((50, 2))
        X[:, 1] = np.linspace(1, 10, 50)
        y = 2.0 * X[:, 1] + np.random.normal(0, 0.1, 50)
        # Introduce clear artificial outlier
        y[25] += 10.0
        beta_hat, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
        cd = cook_distance(X, y, beta_hat)
        self.assertEqual(len(cd), 50)
        self.assertEqual(np.argmax(cd), 25)

    def test_information_criteria(self):
        # Sample size n=30 > e^2 (~7.4), where BIC penalty ln(n)*k > AIC penalty 2*k
        y_true = np.linspace(1.0, 10.0, 30)
        y_pred = y_true + np.random.normal(0, 0.05, 30)
        ic = information_criteria(y_true, y_pred, k_params=3)
        self.assertIn('AIC', ic)
        self.assertIn('BIC', ic)
        self.assertGreater(ic['BIC'], ic['AIC'])


if __name__ == '__main__':
    unittest.main()
