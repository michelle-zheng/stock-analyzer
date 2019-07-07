import stock_api
import mvp
import cml

def main():
    while True:
        cmd = raw_input("Enter 'm' to determine the ideal MVP portfolio. Enter 'c' for CML analysis. Enter 'q' to quit. Enter your command: ").lower()

        if cmd == "q":
            break
        elif not (cmd == "c" or cmd == "m"):
            print("Invalid command. Please try again")
            continue

        # Get the symbols of the stocks being compared
        stock_1 = raw_input("Enter the first stock symbol: ").upper()
        stock_2 = raw_input("Enter the second stock symbol: ").upper()

        stock_1_returns = stock_api.get_stock_returns(stock_1)
        stock_2_returns = stock_api.get_stock_returns(stock_2)

        if cmd == "m":
            pass
        elif cmd == "c":
            # Get return on risk-free asset
            rf_return = None

            while not rf_return:
                rf_return_input = raw_input("Enter the return on the risk-free asset from 0 - 100 (ex. 20 for 20%): ")

                try:
                    rf_return = float(rf_return_input)
                except ValueError:
                    print("Invalid input.")

                if rf_return < 0 or rf_return > 100:
                    rf_return = None
                    print("Enter a value between 0 and 100.")


if __name__ == '__main__':
    main()
