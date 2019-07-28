import stock_api
import numpy
import math


def average_return(stock):
    stock_returns = stock_api.get_stock_returns(stock)
    avg_return = numpy.mean(stock_returns, keepdims = 0)
    return (avg_return + 1) ** 12 - 1;


def variance(stock):
    stock_returns = stock_api.get_stock_returns(stock)
    return 12 * numpy.var(stock_returns, ddof = 1, keepdims = 0)


def covariance(stock_1, stock_2):
    stock_1_returns = stock_api.get_stock_returns(stock_1)
    stock_2_returns = stock_api.get_stock_returns(stock_2)
    return 12 * numpy.cov(stock_1_returns, stock_2_returns)[0][0]


def portfolio_variance(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    return stock_1_proportion ** 2 * variance(stock_1) + stock_2_proportion ** 2 * variance(stock_2) +\
           stock_1_proportion * stock_2_proportion * covariance(stock_1, stock_2)


def portfolio_standard_deviation(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    var = portfolio_variance(stock_1, stock_2, stock_1_proportion, stock_2_proportion)
    return math.sqrt(var) * math.sqrt(12)


def portfolio_return(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    return stock_1_proportion * average_return(stock_1) + stock_2_proportion * average_return(stock_2)




