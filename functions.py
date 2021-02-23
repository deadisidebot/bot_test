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
            if i["member_id"] > 0:
                users.append(i["member_id"])
        output_id = random.choice(users)
        for i in answer["profiles"]:
            if i["id"] == output_id:
                return "@id" + str(output_id) + "(" + i["first_name"] + " " + i["last_name"] + ")"
    except:
        return "бот не имеет права администратора в этой беседе"


def psycho():  # возвращяет стороку с 1000 993 и т.д
    return " ".join([str(i) for i in range(1000, -1, -7)])


def who(peer_id, message):  # возвращят строку с упоминанием кого-то
    text = message.replace("/кто", "")
    return "Я думаю что" + text + " " + send_random(peer_id)


def chance(message):  # возвращяет строку с вероятностью какого-либо события
    text = message.replace("/вероятность", "")
    ran = random.randint(1, 100)
    return "Вероятность " + text + " " + str(ran) + "% "


def iq(message):  # возвращяет обращение + рандомное iq
    text = message.replace("/iq", "")
    ran = random.randint(1, 300)
    return "Я думаю, что" + text + " имеет " + str(ran) + " iq"


def love(peer_id):  # возвращяет 2 человек из беседы
    first_person = send_random(peer_id)
    second_person = send_random(peer_id)
    return first_person + " любит " + second_person


def send_photo(peer_id, attachment):
    vk.messages.send(
        peer_id=peer_id,
        attachment=attachment,
        random_id=get_random_id(),
    )


def random_photo_id():
    return random.choice(["photo-181110264_457239022", "photo-181110264_457239023"])


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

