import math
import numpy as np
import statistics


def mvpAnalysis(stock_1, stock_2):
    weights_0 = np.array(list(range(0, 41))) / float(40)
    weights_1 = 1 - weights_0
    weights = np.array([weights_0, weights_1]).T
    weight1 = weights[0][0]
    weight2 = weights[0][1]
    min_var = statistics.portfolio_variance(stock_1, stock_2, weight1, weight2)
    for w in weights:
        if statistics.portfolio_variance(stock_1, stock_2, w[0], w[1]) < min_var:
            min_var = statistics.portfolio_variance(stock_1, stock_2, w[0], w[1])
            weight1 = w[0]
            weight2 = w[1]

    print ("MVP proportion {:s} : {:.2f} %".format(stock_1, weight1 * 100))
    print ("MVP proportion {:s} : {:.2f} %".format(stock_2, weight2 * 100))
    print ("MVP standard deviation: {:.2f} %".format(math.sqrt(min_var) * 100))
    print ("MVP expected portfolio return: {:.2f} %"
           .format(statistics.portfolio_return(stock_1, stock_2, weight1, weight2) * 100))