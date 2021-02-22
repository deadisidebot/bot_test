from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import time
from datetime import datetime, timedelta

first_call_time = datetime.now()
current_call_time = first_call_time

accessToken = '45c75c77b3e815e782f1851c772fbf12a59ef0a0df673a36bb2a8153616bbcec65a262c5a076eed282e13'
groupId = 181110264


vkBotSession = VkApi(token=accessToken)
longPoll = VkBotLongPoll(vkBotSession, groupId)
vk = vkBotSession.get_api()

def send_message(peer_id, message):
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=get_random_id(),
    )



def k(x):
    peer_id = x
    r = 1000
    while r >= 0:
        send_message(peer_id, r)
        r = r - 7
        time.sleep(1) #таймер 142 сек

f = 0

def kd(x, y, z):
    global f

    peer_id = x
    if z == 0:
        send_message(peer_id, y)
        f = time.perf_counter()
    else:
        s = time.perf_counter()
        if s - f >= 600:
            send_message(peer_id, y)
            f = time.perf_counter()
        else:
            send_message(peer_id, "защита от манука")

#if schet==0:
    # send_message(peer_id, '1000 993 986 979 972 965 958 951 944 937 930 923 916 909 902 895 888 881 874 867 860 853 846 839 832 825 818 811 804 797 790 783 776 769 762 755 748 741734 727 720 713 706 699 692 685 678 671 664 657 650 643 636 629 622 615 608 601 594 587 580 573 566 559 552 545 538 531 524 517 510 503 496 489 482 475 468 461 454 447 440 433 426 419 412 405 398 391 384 377 370 363 356 349 342 335 328 321 314 307 300 293 286 279 272 265 258 251 244 237 230 223 216 209 202 195 188 181 174 167 160 153 146 139 132 125 118 111 104 97 90 83 76 69 62 55 48 41 34 27 20 13 6')
    #f = time.perf_counter()
    #schet = 1
#else:
    #s = time.perf_counter()

    #if s - f >= 600:
        #send_message(peer_id,'1000 993 986 979 972 965 958 951 944 937 930 923 916 909 902 895 888 881 874 867 860 853 846 839 832 825 818 811 804 797 790 783 776 769 762 755 748 741734 727 720 713 706 699 692 685 678 671 664 657 650 643 636 629 622 615 608 601 594 587 580 573 566 559 552 545 538 531 524 517 510 503 496 489 482 475 468 461 454 447 440 433 426 419 412 405 398 391 384 377 370 363 356 349 342 335 328 321 314 307 300 293 286 279 272 265 258 251 244 237 230 223 216 209 202 195 188 181 174 167 160 153 146 139 132 125 118 111 104 97 90 83 76 69 62 55 48 41 34 27 20 13 6')
        #f = time.perf_counter()
    #else:
        #send_message(peer_id, "еще рано")


