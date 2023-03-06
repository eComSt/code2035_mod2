import telebot
import threading
from tanks import Tank
tok = "5614676987:AAFjB8-KJRp2Gp16lMEk2rasjnnoUWP2qME"
bot = telebot.TeleBot(tok)
tanks_mass=[]

@bot.message_handler(commands=["make"])
def make_message(message):
    data=message.text.split()[1:]
    if len(data)!=5:print("not enaugh params")
    if data[0] not in [i.model for i in tanks_mass]:
        try:
            model=data[0]
            armor=int(data[1])
            health=float(data[2])
            min_d=int(data[3])
            max_d=int(data[4])
            tanks_mass.append(Tank(model,armor,health,min_d,max_d))
            tanks_mass[-1].print_info()
            bot.send_message(message.chat.id,tanks_mass[-1].mes)
            tanks_mass[-1].mes=""
        except:bot.send_message(message.chat.id,"Нельзя создать такой танк")
    else: bot.send_message(message.chat.id,"Такой танк уже есть")

@bot.message_handler(commands=["show"])
def show_message(message):
    for i in tanks_mass:
        i.print_info()
        bot.send_message(message.chat.id,i.mes)

@bot.message_handler(commands=["shot"])
def make_message(message):
    global tanks_mass
    data=message.text.split()[1:]
    print(data)
    if len(data)!=2:print("not enaugh params")
    try:
        for i in tanks_mass:
            if i.model==data[0]: t1=i
            if i.model==data[1]: t2=i
        t1.shot(t2)
        bot.send_message(message.chat.id,t1.mes)
        bot.send_message(message.chat.id,t2.mes)
        tanks_mass=[i for i in tanks_mass if i.health>0]
    except:bot.send_message(message.chat.id,"Выстрел не удался")


t = threading.Thread(target=bot.infinity_polling)
t.start()
