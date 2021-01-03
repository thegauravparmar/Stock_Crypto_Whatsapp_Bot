# MARKETSTACK_KEY=d5a5825c280a0ab2ad1761dcbde60e89

# imports
import os  # to access environment variable
import requests  # to call the marketstack api
import json  # to get the data formated

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'


# takes input as stocks name and return last lastest price of the stock
def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY  # stores key in accesskey format
    }
    # creats a complete url
    end_point = "".join(
        [BASE_URL, "tickers/", stock_symbol, "/intraday/latest"])
    # joins url with access key to get the result in json
    api_result = requests.get(end_point, params)
    # print(api_result)
    # stores the data in json_result variable
    json_result = json.loads(api_result.text)
    return{
        # get the data of last keyword from the json format
        "Last_Price": json_result["last"]
    }
# result=get_stock_price("AMZN")  #for testing purposes
# print(result)           #for testing purposes

# sample post request

# http://api.marketstack.com/v1/tickers/AMZN/intraday/latest?access_key=d5a5825c280a0ab2ad1761dcbde60e89
