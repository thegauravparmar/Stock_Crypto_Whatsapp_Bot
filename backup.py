

def process_msg(msg):  # default function to send all the responses
    response = ""
    if msg == "Hi":
        response = "Hello, Welcome to stock market chat bot. Type sym:<stock_symbol> to know the price of stock"
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['Last_Price']
        last_price_str = str(last_price)
        response = "The Stock Pirce of " + stock_symbol + " is: $" + last_price_str
    else:
        response = "Please type Hi to get started"
    return response
