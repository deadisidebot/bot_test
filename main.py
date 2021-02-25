from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import functions as f  # подключаем все функции

accessToken = f.open_txt("access_token.txt")
groupId = 181110264

vkBotSession = VkApi(token=accessToken)
longPoll = VkBotLongPoll(vkBotSession, groupId)

trigger = False

for event in longPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        """
        Если бот не отвечает на сообщения из беседы, то выдайте ему права
        на чтение всей переписки, а лучше сразу права администратора.
        """
        from_id = event.obj["from_id"]  # id пользователя, который отправил сообщение
        peer_id = event.obj["peer_id"]  # peer_id беседы или ЛС, откуда пришло сообщение

        f.message_counter(from_id)

        # lower - это метод приведения к нижнему регистру. Для регистронезависимости.
        message = event.obj["text"].lower()
        # message теперь в нижнем регистре, поэтому все проверки делаем тоже в нижнем регистре
        if message == "zxc":
            f.send_message(peer_id, "qwe")
        elif message == "qwe":
            f.send_message(peer_id, "zxc")
        elif "ауе" in message:
            f.send_message(peer_id, f.open_txt("aue.txt"))
        elif "соня" in message:
            f.send_message(peer_id, "шлюха")
        elif "пик пик пик" in message:
            f.delay_send_message(peer_id, f.open_txt("ramzes.txt"), trigger)
            trigger = True
        elif "1000-7" in message:
            f.delay_send_message(peer_id, f.psycho(), trigger)
            trigger = True
        elif "!рандом" in message:
            f.send_message(peer_id, f.send_random(peer_id))
        elif "ping" in message:
            f.send_message(peer_id, "pong")
        elif "!кто" in message:
            f.send_message(peer_id, f.who(peer_id, message))
        elif "!вероятность" in message:
            f.send_message(peer_id, f.chance(message))
        elif "!iq" in message:
            f.send_message(peer_id, f.iq(message))
        elif "/кто кого" in message:
            f.send_message(peer_id, f.love(peer_id))
        elif "!photo" in message:
            f.send_attachment(peer_id, f.random_photo_id())
        elif "!сообщения" in message:
            f.send_message(peer_id, f.appeal(from_id) + " ваши сообщения: " + str(f.message_counter_read(from_id)))
        elif "!gif" in message:
            f.send_attachment(peer_id, "doc-181110264_658017648")
        elif "!ник" in message:
            f.send_message(peer_id, f.dead_inside_nicks())
        elif "!оцени" in message:
            f.send_message(peer_id, f.estimation(message, from_id))
        elif "лизо" in message:
            f.send_message(peer_id, "шаболда")
        elif "ишма" in message:
            f.send_message(peer_id, "Сильный лидер")
        elif message == "мать":
            f.send_message(peer_id, f.open_txt("mather.txt"))
        # elif "мем" in message:  не работает переделать
        #     functions.send_attachment(peer_id, functions.another_group_photos("voiceovers", 1))
        # photo-174862538_457403123
