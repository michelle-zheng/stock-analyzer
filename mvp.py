import numpy as np
import statistics


def analysis(stock_1, stock_2, monthly_returns):
    # List of weights of stocks
    weights_stock_1 = np.array(list(range(0, 41)))/40.0
    weights_stock_2 = 1 - weights_stock_1
    weights = np.array([weights_stock_1,weights_stock_2]).T

    # Calculate annual mean returns of each stock
    returns = statistics.annual_mean_returns(monthly_returns)

    # Calculate annual covariance
    covariances = statistics.annual_covariances(monthly_returns)

    # Calculate portfolio statistics
    portfolio_returns = statistics.portfolio_returns(weights, returns)
    portfolio_variances = statistics.portfolio_variances(weights, covariances)
    portfolio_sds = statistics.portfolio_standard_deviations(portfolio_variances)

    # Find the minimum variance portfolio
    min_index = 0
    for i in range(len(portfolio_variances)):
        if portfolio_variances[i] < portfolio_variances[min_index]:
            min_index = i

    # Output answer to Part I
    print ("\nMVP proportion {:s} : {:.2f}%".format(stock_1, weights[min_index][0] * 100))
    print ("MVP proportion {:s} : {:.2f}%".format(stock_2, weights[min_index][1] * 100))
    print ("MVP standard deviation: {:.2f}%".format(portfolio_sds[min_index] * 100))
    print ("MVP expected portfolio return: {:.2f}%".format(portfolio_returns[min_index] * 100))