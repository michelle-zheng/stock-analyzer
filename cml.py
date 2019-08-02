import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics


def sharpe_ratios(rf_return, returns, standard_deviations):
    return [(er - rf_return) / sd for er, sd in zip(returns, standard_deviations)]


def analysis(rf_return, stock_1, stock_2, monthly_returns):
    # Find the market portfolio
    market_portfolio_index = 0

    # List of weights of stocks
    weights_stock_1 = np.array(list(range(0, 41))) / 40.0
    weights_stock_2 = 1 - weights_stock_1
    weights = np.array([weights_stock_1, weights_stock_2]).T

    # Calculate annual mean returns of each stock
    returns = statistics.annual_mean_returns(monthly_returns)

    # Calculate annual covariance
    covariances = statistics.annual_covariances(monthly_returns)

    # Calculate stock portfolio statistics
    portfolio_returns = statistics.portfolio_returns(weights, returns)
    portfolio_variances = statistics.portfolio_variances(weights, covariances)
    portfolio_sds = statistics.portfolio_standard_deviations(portfolio_variances)

    # Calculate Sharpe ratios
    portfolio_sharpe_ratios = sharpe_ratios(rf_return, portfolio_returns, portfolio_sds)

    # Find maximum Sharpe ratio
    for i in range(len(portfolio_sharpe_ratios)):
        if portfolio_sharpe_ratios[i] > portfolio_sharpe_ratios[market_portfolio_index]:
            market_portfolio_index = i

    # Case 1: 100% in market portfolio, 0% in risk-free asset
    print("\nCase 1:")
    print("Given proportion invested in risk-free asset: 0%")
    print("Given proportion invested in market portfolio: 100% \n")
    print("Maximum Sharpe ratio: {:.2f}".format(portfolio_sharpe_ratios[market_portfolio_index]))
    print("Market portfolio proportion {:s} : {:.2f}%".format(stock_1, weights[market_portfolio_index][0]*100))
    print("Market portfolio proportion {:s} : {:.2f}%".format(stock_2, weights[market_portfolio_index][1]*100))
    print("Market portfolio expected return: {:.2f}%".format(portfolio_returns[market_portfolio_index] * 100))
    print("Market portfolio standard deviation: {:.2f}%".format(portfolio_sds[market_portfolio_index] * 100))

    # Case 2: 50% in market portfolio, 50% in risk-free asset
    print("\nCase 2:")
    print("Given proportion invested in risk-free asset: 50%")
    print("Given proportion invested in market portfolio: 50%\n")
    print("Portfolio expected return: {:.2f}%".format((0.5 * rf_return + 0.5 * portfolio_returns[market_portfolio_index]) * 100))
    print("Portfolio standard deviation: {:.2f}%".format((0.5 * portfolio_sds[market_portfolio_index]) * 100))

    # Case 3: 150% in market portfolio, -50% in risk-free asset
    print("\nCase 3:")
    print("Given proportion invested in risk-free asset: -50%")
    print("Given proportion invested in market portfolio: 150%\n")
    print("Portfolio expected return: {:.2f}%".format((-0.5 * rf_return + 1.5 * portfolio_returns[market_portfolio_index]) * 100))
    print("Portfolio standard deviation: {:.2f}%\n".format((1.5 * portfolio_sds[market_portfolio_index]) * 100))


    # Efficient frontier
    port_returns = [portfolio_returns[index] for index in range(len(portfolio_returns)) if index % 4 == 0]
    port_sds = [portfolio_sds[index] for index in range(len(portfolio_sds)) if index % 4 == 0]
    port_srs = [portfolio_sharpe_ratios[index] for index in range(len(portfolio_sharpe_ratios)) if index % 4 == 0]

    df = pd.DataFrame([port_returns, port_sds, port_srs]).transpose()
    df.columns = ['Returns', 'Volatility', 'Sharpe Ratio']

    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()