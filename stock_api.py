import unirest


def get_monthly_stock_prices(stock):
    adj_close = []

    # Get response from API call
    response = unirest.get(
        "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data?frequency=1mo&filter=history&period1=1527794500&period2=1561922500&symbol=" + stock,
        headers={
            "Content-Type": "application/json",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "6fa4e1054dmshedd5deb5fce65fcp176a66jsnbd478274f86a"
        }
    )

    # Add adj_close prices to an array
    if response.body['prices']:
        adj_close = [price['adjclose'] for price in reversed(response.body['prices']) if price.get('adjclose')]

    return adj_close




