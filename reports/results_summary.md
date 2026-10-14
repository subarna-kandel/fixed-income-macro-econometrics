# Research & Methodology Summary: Fixed Income & Macro Econometrics

## 1. Executive Overview
This research explores sovereign term structure modeling, macroeconomic equilibrium dynamics, and econometric regression diagnostics. We combine Nelson-Siegel parametric yield curves with cointegration testing on aggregate consumption and income.

## 2. Core Econometric Modules
- **Term Structure Fitting**:
  - The Nelson-Siegel 4-parameter formulation models the yield curve as a combination of Level ($eta_0$), Slope ($eta_1$), and Curvature ($eta_2$).
  - Parametric fit contrasted with cubic splines to examine smoothness versus overfitting trade-offs.
- **Cointegration & Error Correction (ECM)**:
  - Engle-Granger two-step procedure and Johansen test applied to US Personal Consumption Expenditures and Disposable Income.
  - Estimation of dynamic Error Correction Model (ECM) capturing short-run fluctuations around long-run equilibrium.
- **Model Diagnostics & Outlier Analysis**:
  - Multicollinearity evaluation under correlated predictors.
  - Cook's Distance and leverage diagnostics identifying high-influence macroeconomic shocks.

## 3. Results & Empirical Takeaways
- **Yield Curve Interpretability**: The Nelson-Siegel model captures the empirical term structure with economic interpretability, providing stable long-run rate forecasts.
- **Permanent Income Validation**: Real consumption and disposable income are firmly cointegrated ($p < 0.01$), with the ECM speed of adjustment confirming reversion to the cointegrating vector.
- **Robust Inference**: Outlier filtering via Cook's distance prevents single-quarter macro shocks from distorting structural coefficient estimates.
