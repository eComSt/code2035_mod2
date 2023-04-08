#импорт библиотек
import wiki
import vk_api
from course import get_course
from vk_api.longpoll import VkLongPoll, VkEventType
import random
def send(txt):
    vk.messages.send(user_id = user_id,random_id = random_id,message = txt)
#чтения ключа из файла
# with open("key.txt","r") as file:
#     token = file.read()
token = "vk1.a.WszhTQ8I-htDoOKW_lpr_L627mEbRbC69VlvtbwVSAuCo43NNWbJT-CveKkQrJkYN1WlEhsupZXu_BsLQxKJ7ID6Bnxwx5yhpz1bjG3lxJETUozE54AY12q3t0E_B2fHcyDz3b1gDx2_sM7nQLIS7k8UYVL4mZ9BAH16tbz8TLQ_q7kKGVeuPIBTQwiHgorRwSvnQUFFLa_ycHkaVevetQ"
print(token)
# подключение к вк лонгполл
vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1,10**10)
        print(msg)
        if msg == "-эхо":
            ans = "эхо"
        elif msg.startswith("-в"):
            article = msg[2:]
            ans = wiki.get_wiki_article(article)
        elif msg.startswith("-к"):
            article = msg[2:]
            ans = "{0} рублей за 1 доллар\n{1} рублей за 1 евро".format( get_course("R01235"), get_course("R01239"))
        else:
            ans = "Неизвестная комманда"
        send(ans)
