import vk_api,requests,datetime
from bs4 import BeautifulSoup
def course_get():
    today = datetime.today().strftime("%d.%m.%Y")
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    payload = {"date_req":today}
    response = requests.get(url,params = payload)
    xml = BeautifulSoup(response.content,"lxml")
    return str(xml.find("valute",{"id":"R01335"}).value.text)
