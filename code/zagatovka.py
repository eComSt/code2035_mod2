import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5639198841:AAGGyjQM3G2T8xuFU6YotYx7xfUZAvYKwto'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button1=telebot.types.KeyboardButton("Факт")
    button2=telebot.types.KeyboardButton("Стихотворение")
    #button3=
    #button4=
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id,  welcome_text,reply_markup=keyboard)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    keyboard= telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url=telebot.types.InlineKeyboardButton("Перейти",url="https://stihi.ru")
    keyboard.add(button_url)
    bot.send_message(message.chat.id, poem_text,reply_markup=keyboard)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link =  fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(content_types=['text'])
def answear(message):
    if message.text.strip() == "Факт":send_fact(message)
    elif message.text.strip() == "Стихотворение":send_poem(message)

bot.polling()

