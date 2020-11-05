import os, telebot, requests, datetime

bot = telebot.TeleBot(token = os.getenv('TOKEN'))
r = requests.get('https://www.bw.com/exchange/config/controller/website/pricecontroller/getassistprice')
data = r.json()
coins = ['btc','eth','xmr','grin']

def price_coin(arr):
    string = ''
    for i in range(len(arr)):
        price = data ['datas']['usd'][arr[i]]
        string = string + arr[i] + ':' + price + '$' +'\n'
    return string

def lists_coin(arr):
    string = ''
    for i in range(len(arr)):
        string = string + arr[i] + '\n'
    return  string

@bot.message_handler(commands=['start'])
def add_coin(message):
    bot.send_message(message.chat.id,'This bot is for sending the price of a cryptocurrency. It sends it at 10, 14, 18 and 22 hours. List coin:btc, eth, xmr.')
    
    while True:
        time = datetime.datetime.now()
        if time.hour == 10 and time.minute == 00 and time.second == 00 and time.microsecond == 000000:
            bot.send_message(message.chat.id, 'Coins:\n' + price_coin(coins))
        elif time.hour == 13 and time.minute == 00 and time.second == 00 and time.microsecond == 000000:
            bot.send_message(message.chat.id, 'Coins:\n' + price_coin(coins))
        elif time.hour == 16 and time.minute == 00 and time.second == 00 and time.microsecond == 000000:
            bot.send_message(message.chat.id, 'Coins:\n' + price_coin(coins))
        elif time.hour == 19 and time.minute == 00 and time.second == 00 and time.microsecond == 000000:
            bot.send_message(message.chat.id, 'Coins:\n' + price_coin(coins))
        elif time.hour == 22 and time.minute == 00 and time.second == 00 and time.microsecond == 000000:
            bot.send_message(message.chat.id, 'Coins:\n' + price_coin(coins))
            
bot.polling()
