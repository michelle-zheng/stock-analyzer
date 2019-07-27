import math
import statistics
import numpy as np

def mvpAnalysis(stock_1, stock_2):
    weights_0 = np.array(list(range(0,41)))/40
    weights_1 = 1 - weights_0
    weights   = np.array([weights_0,weights_1]).T
    weight1 = weights[0][0]
    weight2 = weights[0][1]
    max_var = statistics.portfolio_variance(stock_1, stock_2, weight1, weight2)
    for w in weights:
        if statistics.portfolio_variance(stock_1, stock_2, w[0], w[1]) > max_var :
            max_var = statistics.portfolio_variance(stock_1, stock_2, w[0], w[1])
            weight1 = w[0]
            weight2 = w[1]

    print ("MVP proportion ", stock_1, " : ", weight1)
    print ("MVP proportion ", stock_2, " : ", weight2)
    print ("MVP standard deviation: ", math.sqrt(max_var))
    print ("MVP expected portfolio return: ", statistics.portfolio_return(stock_1, stock_2, weight1, weight2))