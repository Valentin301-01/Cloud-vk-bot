import vk_api
import random
import time

token = "токен"

vk = vk_api.VkApi(token=token)
bh = vk_api.VkApi(token=token)

vk._auth_token()

print('Бот запущен')
while True:

    try:

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!тест":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Бот работает исправно!",
                           "random_id": random.randint(1, 2147483647)})
            elif body.lower() == 'картинка':
                # Отправляем картинку и текст
                bh.method("messages.send",
                          {"peer_id": id, "message": "Вот твоя картинка!", "attachment": "photo381260583_457370887",
                           "random_id": 0})
            elif body.lower() == "!команды":
                vk.method("messages.send", {"peer_id": id, "message": "Список команд\n!тест\n привет\n кто я?\nкартинка",
                                            "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()),
                                            "random_id": random.randint(1, 2147483647)})
    except Exception as E:

        time.sleep(1)
