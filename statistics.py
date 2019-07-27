import stock_api
import numpy


def average_return(stock):
    stock_returns = stock_api.get_stock_returns(stock)
    return sum(stock_returns)/len(stock_returns)


def variance(stock):
    stock_returns = stock_api.get_stock_returns(stock)
    return numpy.var(stock_returns, ddof = 1)

def covariance(stock_1, stock_2):
    stock_1_returns = stock_api.get_stock_returns(stock_1)
    stock_2_returns = stock_api.get_stock_returns(stock_2)
    return numpy.cov(stock_1_returns, stock_2_returns)


def portfolio_variance(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    return stock_1_proportion ** 2 * variance(stock_1) + stock_2_proportion ** 2 * variance(stock_2) +\
           stock_1_proportion * stock_2_proportion * covariance(stock_1, stock_2)


def portfolio_standard_deviation(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    var = portfolio_variance(stock_1, stock_2, stock_1_proportion, stock_2_proportion)
    return numpy.sqrt(var)


def portfolio_return(stock_1, stock_2, stock_1_proportion, stock_2_proportion):
    return stock_1_proportion * average_return(stock_1) + stock_2_proportion * average_return(stock_2)




