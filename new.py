import vk_api,requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
from course import *
import json
url="https://swapi.dev/api/"
responce=requests.get(url).json()
starships_api=responce.get("starships")
def course_get():
    today = datetime.today().strftime("%d.%m.%Y")
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    payload = {"date_req":today}
    response = requests.get(url,params = payload)
    xml = BeautifulSoup(response.content,"lxml")
    return str(xml.find("valute",{"id":"R01335"}).value.text)
def check_starships(url):
    j=0
    starsh=[]
    for i in range(1,100):
        responce = requests.get(f"{url}/{i}").json()
        if len(responce)>1:
            j+=1
            starsh.append({responce.get("name"):responce.get('max_atmosphering_speed')})
        if j==5:break
    print(starsh)
    st = starsh
    b=0
    for i in st:
        if i[list(i.keys())[0]]=="n/a":i[list(i.keys())[0]]="0"
        print(type(int(i[list(i.keys())[0]])))
        if int(i[list(i.keys())[0]])>b:
            a=list(i.keys())[0]
            b=int(i[list(i.keys())[0]])
    return str(a)+" "+str(b)

with open("key.txt",'r') as file:
    token = file.read()

def get_anekdot():
    try:
        res = requests.get('https://www.anekdot.ru/random/anekdot/')
        res = res.content
        html = BeautifulSoup(res, 'lxml')
        return random.choice(html.find_all(class_='text')).text
    except Exception as e:
        return ("Exception (find):", e)

vk = vk_api.VkApi(token=token)
messages = vk.method("messages.getConversations",{"count":20,"filter":"unanswered"})
while True:
    messages = vk.method("messages.getConversations",{"count":20,"filter":"unanswered"})
    if messages["count"] > 0:
        # pprint(messages)
        user_id = messages["items"][0]["last_message"]["from_id"]
        message_id = messages["items"][0]["last_message"]["id"]
        message_text = messages["items"][0]["last_message"]["text"]
        if message_text.lower() == 'дата':
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":datetime.today().strftime("%d.%m.%y")})
        elif message_text.lower() == 'пинг':
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":"понг."})
        elif message_text.lower() == 'курс':
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":course_get()})
        elif message_text.lower() == 'корабли':
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":check_starships(starships_api)})
        elif message_text.lower() == 'ха':
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":get_anekdot()})
        else:
            vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":  "неизвестная команда"})
