from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
from prediction import prediction_stock

app = Flask(__name__)  # initializing flask app

ID = os.environ.get('TWILIO_ACCOUNT')
TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ID, TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'


def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )


stockarray = ["AXISBANK", "BAJAJAUTO", "BAJAJFINSV", "BAJFINANCE", "BHARTIARTL", "BRITANNIA", "CIPLA", "HDFC", "HDFCBANK",
              "ICICIBANK", "ITC", "KOTAKBANK", "ONGC", "RELIANCE", "SBIN", "SUNPHARMA", "TATAMOTORS", "TATASTEEL", "TCS", "WIPRO"]


def process_msg(msg):  # default function to send all the responses
    response = ""
    if msg == "Hi":
        response = "Hello, Welcome to stock market chat bot. \n \n 1. For Prediction (Indian Stocks) type PREDICTION \n 2. Real Time (International Stocks) type REALTIME"
    elif msg == "REALTIME":
        response = "Type REALTIME:<stock_symbol> to know the price of stock"
    elif 'REALTIME:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['Last_Price']
        last_price_str = str(last_price)
        response = "The Stock Pirce of " + stock_symbol + " is: $" + last_price_str
    elif msg == "PREDICTION":
        response = "Select the required stock from below for prediction. \n Eg. Type '1' for AXISBANK \n\n 1. AXISBANK \n 2. BAJAJ-AUTO \n 3. BAJAJFINSV \n 4. BAJFINANCE \n 5. BHARTIARTL \n 6. BRITANNIA \n 7. CIPLA \n 8. HDFC \n 9. HDFCBANK \n 10. ICICIBANK \n 11. ITC \n 12. KOTAKBANK \n 13. ONGC \n 14. RELIANCE \n 15. SBIN \n 16. SUNPHARMA \n 17. TATAMOTORS \n 18. TATASTEEL \n 19. TCS \n 20. WIPRO"
    elif msg == "1":
        response = prediction_stock(stockarray[0])
    elif msg == "2":
        response = prediction_stock(stockarray[1])
    elif msg == "3":
        response = prediction_stock(stockarray[2])
    elif msg == "4":
        response = prediction_stock(stockarray[3])
    elif msg == "5":
        response = prediction_stock(stockarray[4])
    elif msg == "6":
        response = prediction_stock(stockarray[5])
    elif msg == "7":
        response = prediction_stock(stockarray[6])
    elif msg == "8":
        response = prediction_stock(stockarray[7])
    elif msg == "9":
        response = prediction_stock(stockarray[8])
    elif msg == "10":
        response = prediction_stock(stockarray[9])
    elif msg == "11":
        response = prediction_stock(stockarray[10])
    elif msg == "12":
        response = prediction_stock(stockarray[11])
    elif msg == "13":
        response = prediction_stock(stockarray[12])
    elif msg == "14":
        response = prediction_stock(stockarray[13])
    elif msg == "15":
        response = prediction_stock(stockarray[14])
    elif msg == "16":
        response = prediction_stock(stockarray[15])
    elif msg == "17":
        response = prediction_stock(stockarray[16])
    elif msg == "18":
        response = prediction_stock(stockarray[17])
    elif msg == "19":
        response = prediction_stock(stockarray[18])
    elif msg == "20":
        response = prediction_stock(stockarray[19])
    else:
        response = "Please type Hi to get started"
    return response


@app.route("/", methods=["POST"])  # default route of the program
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return "OK", 200

# TWILIO_ACCOUNT
# TWILIO_TOKEN


# MARKETSTACK_KEY = d5a5825c280a0ab2ad1761dcbde60e89

# AC1456f1794c1d1d2846f997f842fdc094
# 7096a0fe331ddf2da774a9847bea9628
