# import requests module
import sched
import requests

# run BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler

import telepot

import telegram

from pprint import pprint

from telepot.loop import MessageLoop

# get a webpage
# r -> Response object
r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR&extraParams=Bitfinex')

# read the content of the server's response
# use json to access response objects
response = r.json()
eur_price = response['EUR']
usd_price = response['USD']
# a = r.text
# print(a['EUR'])
# eur_price = r.text.EUR
# usd_price = r.text.USD

# use BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

# account test 
# bot = telepot.Bot('5561261260:AAGjGQ8arLymg-OzLaiDcJArjh1JpAOjQwo')
# bot.getMe()

# getUpdates() returns an array of Update objects
# offset=100000001 -> to avoid getting the same old messages 
# response = bot.getUpdates(offset=100000001)
# print(response)

# to monitor the messages
# def handle(msg):
#     pprint(msg)

# MessageLoop(bot, handle).run_as_thread()

# bot.sendMessage(5561261260, 'Hey!')



api_key = "5561261260:AAGjGQ8arLymg-OzLaiDcJArjh1JpAOjQwo"
id = "5487316245"
 
bot = telegram.Bot(token=api_key)

# functions that send texts
def send_coin_price():
    bot.sendMessage(chat_id=id, text='text')
    # f"BTC-USD: {usd_price}\nBTC-EUR: {eur_price}"


# calling add_job() -> add jobs to a scheduler
# interval -> use when I want to run the job at fixed intervals of time 
scheduler.add_job(send_coin_price, 'interval', seconds=1)
#  id='my_job_id'
# scheduler.remove_job('my_job_id')
# scheduler.add_job(send_coin_price, 'cron', second='1')

# scheduler.start(paused=True)


# file:///C:/Users/SAMSUNG/Desktop/3-1/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC/ene419-assignment-1-2022.pdf
# https://min-api.cryptocompare.com/documentation?key=Price&cat=SingleSymbolPriceEndpoint
# https://requests.readthedocs.io/en/latest/user/quickstart/
# https://apscheduler.readthedocs.io/en/latest/userguide.html
# https://telepot.readthedocs.io/en/latest/

# https://ddolcat.tistory.com/746
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=varkiry05&logNo=221257249284
# 