#MARKETSTACK_KEY=d5a5825c280a0ab2ad1761dcbde60e89

#0 explore the ms docs and find relevent code
#1 integrate api

#imports

import os
import requests
import json

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    end_point="".join([BASE_URL, "tickers/" ,stock_symbol, "/intraday/latest"])
    api_result = requests.get(end_point, params)
    print(api_result)
    json_result = json.loads(api_result.text)
    return{
        "Last_Price": json_result["last"]
    }
result=get_stock_price("AMZN")
print(result)
