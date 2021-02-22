from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import functions  # подключаем все функции

accessToken = functions.open_txt("access_token.txt")
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

        # lower - это метод приведения к нижнему регистру. Для регистронезависимости.
        message = event.obj["text"].lower()

        # message теперь в нижнем регистре, поэтому все проверки делаем тоже в нижнем регистре
        if "zxc" in message:
            functions.send_message(peer_id, "qwe")
        elif "qwe" in message:
            functions.send_message(peer_id, "zxc")
        elif "ауе" in message:
            functions.send_message(peer_id, functions.open_txt("aue.txt"))
        elif "соня" in message:
            functions.send_message(peer_id, "шлюха")
        elif "пик пик пик" in message:
            functions.delay_send_message(peer_id, functions.open_txt("ramzes.txt"), trigger)
            trigger = True
        elif "1000-7" in message:
            functions.delay_send_message(peer_id, functions.psycho(), trigger)
            trigger = True
        elif "!рандом" in message:
            functions.send_message(peer_id, functions.send_random(peer_id))
        elif "ping" in message:
            functions.send_message(peer_id, "pong")
