from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price

app = Flask(__name__) 

ID = os.environ.get('TWILIO_ACCOUNT')
TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ID,TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def send_msg(msg,recipient):
    client.messages.create(
        from_ = TWILIO_NUMBER,
        body = msg,
        to = recipient
    )

def process_msg(msg):
    response = ""
    if msg == "hi":
        response ="Hello, Welcome to stock market chat bot. Type sym:<stock_symbol> to know the price of stock"
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price=get_stock_price(stock_symbol)
        last_price=stock_price['Last_Price']
        last_price_str = str(last_price)
        response="The Stock Pirce of " + stock_symbol + " is: $" + last_price_str
    else:
        response = "Please type hi to get started"
    return response



@app.route("/",methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    return "OK",200

#TWILIO_ACCOUNT
#TWILIO_TOKEN


# import client from twilio
# initialise client
# write a function to process msg
# write a function to send messag
# generate a response
# check response on whstapp
# MARKETSTACK_KEY = d5a5825c280a0ab2ad1761dcbde60e89

#AC1456f1794c1d1d2846f997f842fdc094
#7096a0fe331ddf2da774a9847bea9628
#AC1456f1794c1d1d2846f997f842fdc094