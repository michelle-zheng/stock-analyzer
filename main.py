import stock_api
import mvp
import cml
import pandas as pd


def main():
    while True:
        cmd = raw_input("Enter 'c' for 2-stock comparison. Enter 'b' for "
                        "the answer to the bonus question. Enter 'q' to quit."
                        " Enter your command: ").lower()

        if cmd == "q":
            break
        elif not (cmd == "b" or cmd == "c"):
            print("Invalid command. Please try again")
            continue

        # Perform 2-stock comparison
        if cmd == "c":
            # Get the symbols of the stocks being compared
            stock_1 = raw_input("Enter the first stock symbol: ").upper()
            stock_2 = raw_input("Enter the second stock symbol: ").upper()

            # Get return on risk-free asset
            # Must be a float between 1 and 100
            rf_return = None

            while not rf_return:
                rf_return_input = raw_input(
                    "Enter the return on the risk-free asset from 0 - 100 "
                    "(ex. 20 for 20%): ")

                try:
                    rf_return = float(rf_return_input)
                except ValueError:
                    print("Invalid input.")

                if rf_return < 0 or rf_return > 100:
                    rf_return = None
                    print("Enter a value between 0 and 100.")

            # Convert rf_return to a decimal
            rf_return /= 100

            # Get the adjusted close monthly stock prices from the API
            stock_1_monthly_prices = stock_api.get_monthly_stock_prices(stock_1)
            stock_2_monthly_prices = stock_api.get_monthly_stock_prices(stock_2)

            # Put the prices into a data frame and convert into monthly returns
            d = {'stock_1': stock_1_monthly_prices, 'stock_2': stock_2_monthly_prices}
            data = pd.DataFrame(d)
            monthly_returns = data.pct_change()

            # Analysis for Part I
            print("\nAnswer to Part I")
            mvp.analysis(stock_1, stock_2, monthly_returns)

            # Analysis for Part II
            print("\nAnswer to Part II")
            cml.analysis(rf_return, stock_1, stock_2, monthly_returns)

        # Output the market portfolio of 5-10 stocks that when split with
        # even proportions has an expected return of >= 10% and a portfolio
        # standard deviation of <= 5%
        elif cmd == "b":
            print("Answer to Bonus")


if __name__ == '__main__':
    main()
