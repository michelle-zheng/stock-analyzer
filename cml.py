#import mvp
import math
import numpy

def analysis(stock_1, stock_2, rf_return):
    stock_1_returns = stock_api.get_stock_returns(stock_1)
    stock_2_returns = stock_api.get_stock_returns(stock_2)

    stock_1_avg_ret = numpy.mean(stock_1_returns)
    stock_2_avg_ret = numpy.mean(stock_2_returns)
    #stock_1_proportion = mvp.get_stock_proportion(stock_1)
    #stock_2_proportion = mvp.get_stock_proportion(stock_2)
    stock_1_var = numpy.var(stock_1_returns, ddof = 1)
    stock_2_var = numpy.var(stock_2_returns, ddof = 1)
    covariance = numpy.cov(stock_1_returns, stock_2_returns)
    
    mkt_port_return = stock_1_avg_ret * stock_1_proportion + stock_2_avg_ret * stock_2_proportion
    mkt_variance = stock_1_proportion ** 2 * stock_1_var + stock_2_proportion ** 2 * stock_2_var + stock_1_proportion * stock_2_proportion * covariance
    mkt_stdev = sqrt(mkt_variance)
    sharpe_ratio = (mkt_port_return - rf_return) / mkt_stdev

    print("Case 1:")
    print("Given proportion invested in risk-free asset: 0%\nGiven prpertion invested in market portfolio: 100%\n\n")
    print("Maximum Sharpe ratio: ",sharpe_ratio)
    print("Market portfolio proportion ", stock_1, " : ", stock_1_proportion)
    print("Market portfolio proportion ", stock_2, " : ", stock_2_proportion)
    print("Market portfolio expected return: ", mkt_port_return)
    print("Market portfolio standard deviation: ", mkt_stdev)


    print("Case 2:")
    print("Given proportion invested in risk-free asset: 50%\nGiven prpertion invested in market portfolio: 50%\n\n")
    port_exp_return = 50% * rf_return + 50% * mkt_port_return
    print("Portfolio expected return: ", port_exp_return)
    port_stdev = 50% * mkt_stdev
    print("Portfolio standard deviation: ", port_stdev)

    print("Case 3:")
    print("Given proportion invested in risk-free asset: -50%\nGiven prpertion invested in market portfolio: 150%\n\n")
    port_exp_return = -50% * rf_return + 150% * mkt_port_return
    print("Portfolio expected return: ", port_exp_return)
    port_stdev = 150% * mkt_stdev
    print("Portfolio standard deviation: ", port_stdev)
