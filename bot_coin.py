import os, telebot, requests, schedule, time, threading, datetime

bot = telebot.TeleBot(token = os.getenv('TOKEN'))
r = requests.get('https://www.bw.com/exchange/config/controller/website/pricecontroller/getassistprice')
data = r.json()
coins = ['btc','eth','xmr','grin']
message_id = []
# file_id = open("id.txt",'a+',encoding ='utf-8')

def price_coin(arr):
    string = ''
    for i in range(len(arr)):
        price = data ['datas']['usd'][arr[i]]
        string_coin = arr[i]
        string = string + string_coin.upper() + ': ' + price + '$' +'\n'
    return string

def lists_coin(arr):
    string = ''
    for i in range(len(arr)):
        string = string + arr[i] + ' '
    return  string

def print_date():
    date = ''
    today = datetime.date.today()
    date = 'Date: {}.{}.{}\n'.format(today.day,today.month,today.year)
    return date

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,'This bot is for sending the price of a cryptocurrency. It sends it at 10, 13, 16, 19 and 22 hours. List coin:' + lists_coin(coins) + '.')
    if message.chat.id not in message_id:
        message_id.append(message.chat.id)
    # file_id.write('{}\n'.format(message.chat.id))

def print_coin():
    for i in range(len(message_id)):
        bot.send_message(message_id[i], 'Coins:\n' + price_coin(coins) + print_date())
        
def run_func():   
    schedule.every().day.at("10:00").do(print_coin)
    schedule.every().day.at("13:00").do(print_coin)
    schedule.every().day.at("16:00").do(print_coin)
    schedule.every().day.at("19:00").do(print_coin)
    schedule.every().day.at("22:00").do(print_coin)

    while True:
        schedule.run_pending()
        time.sleep(1)

th = threading.Thread(target = run_func, args = ())
th.start()

bot.polling()
# file_id.close() 