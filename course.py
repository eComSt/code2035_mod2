import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, features="xml")


def get_course(valute):
    for currency in xml.find_all("Valute"):
        currency_name = currency.Name.text.lower()
        if currency_name == valute.lower():
            return currency.Nominal.text, currency.Value.text
    return None,None
