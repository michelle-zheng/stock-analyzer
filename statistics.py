import numpy as np


# Calculates annual mean returns of returns stored in data frame
def annual_mean_returns(monthly_returns):
    annual_mean_rets = (1 + monthly_returns.mean())**12 - 1
    return np.array(annual_mean_rets)


# Calculates annual covariances of returns stored in data frame
def annual_covariances(monthly_returns):
    annual_covs = monthly_returns.cov() * 12
    return np.array(annual_covs)


# Calculates the expected returns for a 2-stock portfolio
def portfolio_returns(weights, returns):
    return [w[0] * returns[0] + w[1] * returns[1] for w in weights]


# Calculates the variances for a 2-stock portfolio
def portfolio_variances(weights, covariances):
    return [w[0]**2 * covariances[0, 0] + w[1]**2 * covariances[1, 1] + 2 * w[0] * w[1] * covariances[0, 1] for w in weights]


# Calculates the standard deviation for a 2-stock portfolio
def portfolio_standard_deviations(portfolio_variances):
    return [np.sqrt(v) for v in portfolio_variances]






