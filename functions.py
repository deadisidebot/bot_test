from vk_api import VkApi
from vk_api.utils import get_random_id  # для get_random_id()
import random
import time


def open_txt(txt_name):  # возвращяет текст из тестового файла
    file = open("txt\\" + txt_name, "r", encoding="utf-8")  # txt\ папка где все лежит
    output = file.read()
    file.close()
    return output


accessToken = open_txt("access_token.txt")
groupId = 181110264

vkBotSession = VkApi(token=accessToken)
vk = vkBotSession.get_api()


def send_message(peer_id, message):  # отправляет сообщениие
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=get_random_id(),
    )


def send_random(peer_id):  # возвращяет обращение к любому участнику беседы(нужны права администратора для бота)
    try:
        answer = vk.messages.getConversationMembers(
            peer_id=peer_id,
        )
        users = []
        for i in answer["items"]:
            users.append(i["member_id"])
        return "@id" + str(random.choice(users))
    except:
        return "бот не имеет права администратора в этой беседе"


def psycho():
    return " ".join([str(i) for i in range(1000, -1, -7)])


def delay_send_message(peer_id, text_message, trigger):
    global f
    if not trigger:
        send_message(peer_id, text_message)
        f = time.perf_counter()
    else:
        s = time.perf_counter()
        if s - f >= 600:
            send_message(peer_id, text_message)
            f = time.perf_counter()
        else:
            send_message(peer_id, "защита от манука")
