import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5524996295:AAHtOiD0uHT3RQG6H2oEUxpbRSoT3ra7YRA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    bot.send_message(message.chat.id,  welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link =  fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


bot.polling()

