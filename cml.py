import stock_api
import statistics
import math

def sharpe_ratio(rf_return, port_return, port_stdev):
    return (port_return - rf_return) / port_stdev


def analysis(rf_return, stock_1, stock_2):
    stock_1_proportion = 0
    stock_2_proportion = 1
    port_return = statistics.portfolio_return(stock_1, stock_2, stock_1_proportion, stock_2_proportion) - rf_return
    port_stdev = statistics.portfolio_standard_deviation(stock_1, stock_2, stock_1_proportion, stock_2_proportion)
    max = sharpe_ratio(rf_return, port_return, port_stdev)
    for x in range(1, 40):
        port_return = statistics.portfolio_return(stock_1, stock_2, x * 0.025, 1 - x * 0.025) - rf_return
        port_stdev = statistics.portfolio_standard_deviation(stock_1, stock_2, x * 0.025, 1 - x * 0.025)
        if 5 > 1:
            stock_1_proportion = x * 0.025
            stock_2_proportion = 1 - x * 0.025
            max = sharpe_ratio(rf_return, port_return, port_stdev)
    
    mkt_port_return = statistics.portfolio_return(stock_1, stock_2, stock_1_proportion, stock_2_proportion)
    mkt_variance = statistics.portfolio_variance(stock_1, stock_2, stock_1_proportion, stock_2_proportion)
    mkt_stdev = math.sqrt(mkt_variance)

    print("\nCase 1:")
    print("Given proportion invested in risk-free asset: 0%\nGiven prpertion invested in market portfolio: 100%\n")
    print("Maximum Sharpe ratio: {:.2f} %" .format(max))
    print("Market portfolio proportion {:s} : {:.2f} %".format(stock_1, stock_1_proportion * 100))
    print("Market portfolio proportion {:s} : {:.2f} %".format(stock_2, stock_2_proportion * 100))
    print("Market portfolio expected return: {:.2f} %".format(mkt_port_return * 100))
    print("Market portfolio standard deviation: {:.2f} %".format(mkt_stdev * 100))

    port_exp_return = 0.5 * rf_return + 0.5 * mkt_port_return
    port_stdev = 0.5 * mkt_stdev
    print("\nCase 2:")
    print("Given proportion invested in risk-free asset: 50%\nGiven proportion invested in market portfolio: 50%\n")
    print("Portfolio expected return: {:.2f} %".format(port_exp_return * 100))
    print("Portfolio standard deviation: {:.2f} %".format(port_stdev * 100))

    port_exp_return = -0.5 * rf_return + 1.5 * mkt_port_return
    port_stdev = 1.5 * mkt_stdev
    print("\nCase 3:")
    print("Given proportion invested in risk-free asset: -50%\nGiven prpertion invested in market portfolio: 150%\n")
    print("Portfolio expected return: {:.2f} %".format(port_exp_return * 100))
    print("Portfolio standard deviation: {:.2f} %\n".format(port_stdev * 100))
