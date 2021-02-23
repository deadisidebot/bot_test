from vk_api import VkApi
from vk_api.utils import get_random_id  # для get_random_id()
import random
import time
import sqlite3


def open_txt(txt_name):  # возвращяет текст из тестового файла
    file = open("txt/" + txt_name, "r", encoding="utf-8")  # txt\ папка где все лежит
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


def appeal(from_id):
    answer = vk.users.get(
        user_ids=from_id,
    )
    return "@id" + str(from_id) + "(" + answer[0]["first_name"] + " " + answer[0]["last_name"] + ")"


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

def dinicks():
    niks = open_txt("dinick.txt")
    text = niks.split(',')
    ans = ' '
    secondint = random.randint(3, 6)
    for i in range(1, secondint):
        fv = random.choice(text)
        ans = ans + ' ' + fv
    return ans


def send_photo(peer_id, attachment):  # отправляет фото
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


def read_db(): #кто это такое 
    connection = sqlite3.connect("profiles.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM id_table").fetchall()
    connection.close()
    return result


def message_counter_read(from_id):
    connection = sqlite3.connect("profiles.db")
    cursor = connection.cursor()
    message_count = list(cursor.execute("SELECT * FROM id_table WHERE id = ?", [str(from_id)], ))[0][1]
    connection.close()
    return message_count


def message_counter(from_id):
    if from_id > 0:
        in_base = False
        result = read_db()

        for i in result:
            if i[0] == from_id:
                in_base = True
                break

        connection = sqlite3.connect("profiles.db")
        cursor = connection.cursor()

        if not in_base:
            cursor.execute("INSERT INTO id_table(id, message_count) VALUES(?, ?)", (from_id, 1,))
        else:
            message_count = message_counter_read(from_id) + 1
            cursor.execute("UPDATE id_table SET message_count = ? WHERE id = ?", (message_count, from_id,))

        connection.commit()
        connection.close()
