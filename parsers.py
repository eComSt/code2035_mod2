
from tkinter import *
import requests
import random 
from bs4 import BeautifulSoup
def ex(event=None):
    root.destroy()
root = Tk()
root.geometry('500x200')
root.protocol('WM_DELETE_WINDOW', ex)
root.attributes('-alpha',1)
root.configure(bg='black')
txt = Text(root,fg='lightgreen',bg='black',relief='groove',font=("Arial", 10), width=81, height=20)
txt.place(x=2,y=2)
root.bind("<q>",ex)

def get_weather():
    ans=""
    try:
        city_id = 1496747
        appid="336d96b279417cabdba8d4608cebced6"
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print(data)
        return "\n".join(["cyty:"+data["name"],"tempreture:"+str(data["main"]["temp"])])
    except Exception as e:
        return ("Exception (find):", e)
    
def get_data():
    try:
        res = requests.get('https://calend.online/holiday/')
        a=res.text.split("<h2>Праздники сегодня <small>полный список</small><")[1].split("</ul>")[0]
        a=a.split('<ul class="holidays-list">')[1]
        a=a.split("<li>\n")
        a=[i.strip(' qwertyuiop[]asdfghjkl;"zxcvbnm,./>/<=-\t\n') for i in a]
        a=[i.split("<")[0] for i in a]
        a=[i.strip(' qwertyuiop[]asdfghjkl;"zxcvbnm,./>/<=-\t\n') for i in a]
        a="\n".join(a)
    except Exception as e:
        return ("Exception (find):", e)
    return a

def get_data_bs():
    try:
        res = requests.get('https://calend.online/holiday/')
        res = res.content
        html = BeautifulSoup(res, 'lxml')
        return "\n".join([li.text.strip() for li in html.select('li') if "Праздники" not in li.text])
    except Exception as e:
        return ("Exception (find):", e)

def get_anekdot():
    try:
        res = requests.get('https://www.anekdot.ru/random/anekdot/')
        res = res.content
        html = BeautifulSoup(res, 'lxml')
        return random.choice(html.find_all(class_='text')).text
    except Exception as e:
        return ("Exception (find):", e)

    
def printw(f):
    txt.insert(1.0,f())

printw(get_data)

while True:
    root.update()
    root.attributes('-topmost', True)
