StockMarket_Whatsapp_ChatBot_Python ( Crypto Will be added in Newer Version )


Details of the files:

1. app.py is the main script to execute the bot.
2. marketstack.py is the file of marketstack functions and api.
3. Procfile (Do not Do anything to it ). It is the file to host the project on heroku server.
4. requirement.txt contains all the required assets. To update this file run the following command
    ```pip freeze > requirements.txt```
5. venv is the virtual environment in flask which will help to run the bot.


Soon the details to run the bot will be added

Set Up the bot:

1. Install Virtual Enviroment
```pip install virtualenv```
2. Install all the dependencies
    ```pip install twilio```
    ```pip install flask```
    ```pip install requests```
3. Set requirements.txt file
    ```pip freeze > requirements.txt```


How to Start

1. Open Bash
2. Use command
```. venv/Scripts/activate```
3. Start
    ```export FLASK_APP=app.py```
4. Export the Keys
    ```export TWILIO_ACCOUNT=AC1456f1794c1d1d2846f997f842fdc094```
    ```export TWILIO_TOKEN=7096a0fe331ddf2da774a9847bea9628```
    ```export MARKETSTACK_KEY=d5a5825c280a0ab2ad1761dcbde60e89```

