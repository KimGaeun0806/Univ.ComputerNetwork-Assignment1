import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from telegram.ext import Updater, CommandHandler
import telegram
from datetime import datetime

# use BackgroundScheduler
scheduler = BackgroundScheduler()

api_key = "5561261260:AAGjGQ8arLymg-OzLaiDcJArjh1JpAOjQwo"
id = "5487316245"

# use telegram to access the bot account
bot = telegram.Bot(token=api_key)

# open the coinPrice.csv file in write format and save it to f
f = open("coinPrice.csv", "w")

# make file header
f.write("Date, BTC-USD, BTC-EUR\n")

# functions that send texts
def send_coin_price():
    # get a webpage
    # r -> Response object
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')

    # read the content of the server's response
    # use json to access response objects
    response = r.json()
    eur_price = response['EUR']
    usd_price = response['USD']

    # send messages
    bot.sendMessage(chat_id=id, text=f"BTC-USD: {usd_price}\nBTC-EUR: {eur_price}")

    # store data in csv file 
    f.write(str(datetime.now()) + ',' + str(usd_price) + ',' + str(eur_price) + '\n')

    # function that works when the stop command is executed
    def stop(update, context):
        scheduler.remove_job('my_job_id')
        f.close()
        
    updater = Updater(token=api_key, use_context=True)

    # Run the stop function when /stop is entered
    stop_handler = CommandHandler('stop', stop)
    updater.dispatcher.add_handler(stop_handler)

    # start updater
    updater.start_polling()
    updater.idle()

# set timezone to remove warning
scheduler = BlockingScheduler(timezone='Asia/Seoul')

# calling add_job() -> add jobs to a scheduler
# cron -> use when run the job periodically at certain times of day
scheduler.add_job(send_coin_price, 'cron', second='1', id='my_job_id')

# start the scheduler
scheduler.start()
